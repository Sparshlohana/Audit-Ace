from flask import Flask, request, jsonify
from PIL import Image
from io import BytesIO
import pytesseract
import os
import csv
import re
from cryptography.fernet import Fernet

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def save_bill_proof(entry_id, bill_file, proof_file):
    # Assuming the files are saved in a directory named 'bills_and_proofs'
    directory = 'bills_and_proofs'
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Encrypt the files
    with open(bill_file, 'rb') as file:
        bill_data = file.read()
    encrypted_bill_data = cipher_suite.encrypt(bill_data)

    with open(proof_file, 'rb') as file:
        proof_data = file.read()
    encrypted_proof_data = cipher_suite.encrypt(proof_data)

    # Save the encrypted files
    encrypted_bill_file = os.path.join(directory, f'{entry_id}_bill.enc')
    encrypted_proof_file = os.path.join(directory, f'{entry_id}_proof.enc')

    with open(encrypted_bill_file, 'wb') as file:
        file.write(encrypted_bill_data)

    with open(encrypted_proof_file, 'wb') as file:
        file.write(encrypted_proof_data)


app = Flask(__name__)

def convert_to_png(input_image):
    try:
        img = Image.open(input_image)
        if img.format != 'PNG':
            output_buffer = BytesIO()
            img.save(output_buffer, format='PNG')
            output_buffer.seek(0)
            return output_buffer
        return img
    except Exception as e:
        print("Error:", e)
        return None

def extract_text_from_image(image_buffer):
    try:
        text = pytesseract.image_to_string(image_buffer)
        return text
    except Exception as e:
        print("Error:", e)
        return None

# Function to extract details from text
def extract_details(text, is_manual=False):
    # Adjusted regular expression patterns
    date_pattern = r"date-(\d{2}-\d{2}-\d{4})"
    account_no_pattern = r"a/c no-(\d+)"
    amount_pattern = r"total amount-(\d+(?:\.\d{1,2})?)"

    details = {}
    if is_manual:
        details['m_date'] = re.search(date_pattern, text).group(1) if re.search(date_pattern, text) else None
        details['m_dr_ac_no'] = re.search(account_no_pattern, text).group(1) if re.search(account_no_pattern, text) else None
        details['m_amt'] = re.search(amount_pattern, text).group(1) if re.search(amount_pattern, text) else None
        details['m_cr_ac_no'] = 'ABCDE1234567' # Default credited account number for manual entries
    else:
        details['r_date'] = re.search(date_pattern, text).group(1) if re.search(date_pattern, text) else None
        details['r_amt'] = re.search(amount_pattern, text).group(1) if re.search(amount_pattern, text) else None
        # Assuming the account number is the only 12-digit number found
        account_numbers = re.findall(account_no_pattern, text)
        details['r_dr_ac_no'] = account_numbers[0] if account_numbers and len(account_numbers[0]) == 12 else None
        details['r_cr_ac_no'] = 'ABCDE1234567' if details['r_dr_ac_no'] == 'ABCDE1234567' else None

    return details

entry_id_counter = 1

def passing_reciept_entry(bill_details, is_manual=False):
    global entry_id_counter
    csv_file = 'bills.csv' if not is_manual else 'manual_entries.csv'
    header = ['id', 'date', 'dr_ac_no', 'cr_ac_no', 'total_amount']
    if not os.path.isfile(csv_file):
        with open(csv_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
    # Check for duplicate entries
    with open(csv_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['date'] == bill_details['p_date'] and \
               row['dr_ac_no'] == bill_details['p_dr_ac_no'] and \
               row['total_amount'] == bill_details['p_amt']:
                return jsonify({'error': 'Duplicate entry found.'}), 400
    # Add new entry
    with open(csv_file, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writerow({
            'id': entry_id_counter,
            'date': bill_details['p_date'],
            'dr_ac_no': bill_details['p_dr_ac_no'],
            'cr_ac_no': bill_details['p_cr_ac_no'],
            'total_amount': bill_details['p_amt']
        })
    entry_id_counter += 1
    # Blockchain handling
    block_data = {
        'id': entry_id_counter - 1,
        'date': bill_details['p_date'],
        'dr_ac_no': bill_details['p_dr_ac_no'],
        'cr_ac_no': bill_details['p_cr_ac_no'],
        'total_amount': bill_details['p_amt']
    }
    blockchain.add_block(block_data)
save_bill_proof()

@app.route('/upload', methods=['POST'])
def upload_images():
    if 'payment_bill' not in request.files or 'proof_for_payment_bill' not in request.files:
        return jsonify({'error': 'Missing files'}), 400

    payment_bill = request.files['payment_bill']
    proof_for_payment_bill = request.files['proof_for_payment_bill']

    png_payment_bill = convert_to_png(payment_bill)
    png_proof_for_payment_bill = convert_to_png(proof_for_payment_bill)

    payment_text = extract_text_from_image(png_payment_bill)
    proof_text = extract_text_from_image(png_proof_for_payment_bill)

    bill_details = extract_details(payment_text)
    proof_details = extract_details(proof_text)

    if bill_details['p_date'] == proof_details['pp_date'] and \
       bill_details['p_dr_ac_no'] == proof_details['pp_dr_ac_no'] and \
       bill_details['p_amt'] == proof_details['pp_amt'] and \
       bill_details['p_cr_ac_no'] == proof_details['pp_cr_ac_no']:
        passing_reciept_entry(bill_details)
        return jsonify({'message': 'Bill and proof details matched and entry passed.'}), 200
    else:
        return jsonify({'error': 'Bill and proof details do not match.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
@app.route('/manual_entry', methods=['POST'])


def manual_entry():
    if 'm_date' not in request.form or 'm_dr_ac_no' not in request.form or 'm_amt' not in request.form or 'm_cr_ac_no' not in request.form or 'm_proof' not in request.files:
        return jsonify({'error': 'Missing fields or files'}), 400

    m_date = request.form['m_date']
    m_dr_ac_no = request.form['m_dr_ac_no']
    m_amt = request.form['m_amt']
    m_cr_ac_no = request.form['m_cr_ac_no']
    m_proof = request.files['m_proof']

    png_m_proof = convert_to_png(m_proof)
    proof_text = extract_text_from_image(png_m_proof)
    proof_details = extract_details(proof_text)

    if m_date == proof_details['p_date'] and \
       m_dr_ac_no == proof_details['p_dr_ac_no'] and \
       m_amt == proof_details['p_amt'] and \
       m_cr_ac_no == proof_details['p_cr_ac_no']:
        bill_details = {
            'p_date': m_date,
            'p_dr_ac_no': m_dr_ac_no,
            'p_amt': m_amt,
            'p_cr_ac_no': m_cr_ac_no
        }
        passing_reciept_entry(bill_details)
        return jsonify({'message': 'Manual entry details matched and entry passed.'}), 200
    else:
        return jsonify({'error': 'Manual entry details do not match.'}), 400
'''potential errorsMissing Initialization of blockchain: It seems that you're trying to use a blockchain object in the passing_reciept_entry() function, but the blockchain object is not defined in the provided code. You need to initialize and define the blockchain object somewhere in your code before using it.
Function Call Without Arguments: In the line save_bill_proof(), you're calling the save_bill_proof() function without providing any arguments. This will result in a TypeError. You should remove this line if it's not meant to be there, or provide the appropriate arguments.
Incorrect Key Usage: When encrypting and decrypting data using Fernet, you should use the same key for encryption and decryption. Ensure that you store and use the key securely and consistently throughout your application.
File Path Handling: If you're not receiving file paths directly from a user interface but instead handling file uploads within the Flask application, you need to save the uploaded files to a temporary location on the server and then pass the file paths to the functions that require them, such as save_bill_proof().
Flask Debug Mode: When running Flask in debug mode (app.run(debug=True)), ensure that you're not exposing sensitive information or running in a production environment, as debug mode can expose debugging information and pose security risks.'''
#add code to handle that the bills are not equal to proofs as in pngs , one shouldn't be uploading 2 same docs 
#ADD rs sign for identifying amount instead of just numbers
#send the bills to a blockchain as well as a seperate chain, all bills and proofs duos with their corresponding ids or 
#just maintain the audit chain to have bill and proof data along with journal entry data and same for block chain