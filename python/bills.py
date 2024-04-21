from flask import Flask, request, jsonify
from PIL import Image
from io import BytesIO
import pytesseract
import os
import csv
import re
from cryptography.fernet import Fernet
from flask_cors import CORS
import logging
import requests
import base64

# Configure logging
logging.basicConfig(filename='app.log', level=logging.DEBUG)

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Initialize entry ID counter
entry_id_counter = 1


from PIL import Image
import base64
import io
import logging

def convert_to_png(input_image):
    try:
        img = Image.open(input_image)
        if img.format != 'PNG':
            # Convert the image to PNG format
            output_buffer = io.BytesIO()
            img.save(output_buffer, format='PNG')
            output_buffer.seek(0)
            # Convert the image data to base64
            base64_image = base64.b64encode(output_buffer.getvalue()).decode('utf-8')
            # Return the base64 image in the correct format
            return f"data:image/png;base64,{base64_image}"
        else:
            # Convert the image data to base64
            output_buffer = io.BytesIO()
            img.save(output_buffer, format='PNG')
            output_buffer.seek(0)
            base64_image = base64.b64encode(output_buffer.getvalue()).decode('utf-8')
            # Return the base64 image in the correct format
            return f"data:image/png;base64,{base64_image}"
    except Exception as e:
        logging.error(f"Error converting image to PNG: {e}")
        return None

        logging.error(f"Error converting image to PNG: {e}")
        return None



# Function to extract text from image
def extract_text_from_image(image_buffer):
    try:
        # Define the API endpoint
        api_url = "https://api.ocr.space/parse/image"
        
        # Define the API key
        api_key = "K85390226988957"
        
        # Define the headers for the API request
        headers = {
            'apikey': api_key,
        }

        # Define the data for the API request
        data = {
            'base64Image': image_buffer,
            'language': 'eng',
            'isOverlayRequired': False,
            'filetype': 'PlainText',    
            'iscreatesearchablepdf': 'false',
            'issearchablepdfhidetextlayer': 'false',
        }
        
        # Make the API request
        response = requests.post(api_url, headers=headers, data=data)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the response to extract the text
            result = response.json()
            text = result['ParsedResults'][0]['ParsedText']
            logging.debug(f"Extracted text: {text}") # Log extracted text
            return text
        else:
            logging.error(f"Error extracting text from image: {response.text}")
            return None
    except Exception as e:
        logging.error(f"Error extracting text from image: {e}")
        return None


# Function to extract details from text
def extract_details(text, is_manual=False):
    # Adjusted regular expression patterns
    date_pattern = r"date-(\d{2})-(\d{2})-(\d{4})"
    account_no_pattern = r"a/c no-(\d{12})"
    amount_pattern = r"total amount-₹\.(\d+(?:\.\d{1,2})?)"

    details = {}
    if is_manual:
        details['m_date'] = re.search(date_pattern, text).group() if re.search(date_pattern, text) else None
        details['m_dr_ac_no'] = re.search(account_no_pattern, text).group(1) if re.search(account_no_pattern, text) else None
        details['m_amt'] = re.search(amount_pattern, text).group(1) if re.search(amount_pattern, text) else None
        details['m_cr_ac_no'] = 'ABCDE1234567' # Default credited account number for manual entries
    else:
        details['p_date'] = re.search(date_pattern, text).group() if re.search(date_pattern, text) else None
        details['p_amt'] = re.search(amount_pattern, text).group(1) if re.search(amount_pattern, text) else None
        # Assuming the account number is the only 12-digit number found
        account_numbers = re.findall(account_no_pattern, text)
        details['p_dr_ac_no'] = account_numbers[0] if account_numbers and len(account_numbers[0]) == 12 else None
        details['p_cr_ac_no'] = 'ABCDE1234567' if details['p_dr_ac_no'] == 'ABCDE1234567' else None
    logging.debug(f"Extracted details: {details}") # Log extracted details
    return details

# Function to save bill and proof files
def save_bill_proof(entry_id, bill_file, proof_file):   
    try:
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
    except Exception as e:
        logging.error(f"An error occurred: {e}")

# Function to pass receipt entry
def passing_receipt_entry(bill_details, is_manual=False):
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
    # Blockchain handling - assuming this is defined elsewhere in the code
    # block_data = {
    #     'id': entry_id_counter - 1,
    #     'date': bill_details['p_date'],
    #     'dr_ac_no': bill_details['p_dr_ac_no'],
    #     'cr_ac_no': bill_details['p_cr_ac_no'],
    #     'total_amount': bill_details['p_amt']
    # }
    # blockchain.add_block(block_data)

# Route for uploading images and processing
@app.route('/upload', methods=['POST'])
def upload_images():
    try:
        if 'payment_bill' not in request.files or 'proof_for_payment_bill' not in request.files:
            logging.error('Missing files in request')
            return jsonify({'error': 'Missing files'}) ,400

        payment_bill = request.files['payment_bill']
        proof_for_payment_bill = request.files['proof_for_payment_bill']

        if payment_bill.filename == '' or proof_for_payment_bill.filename == '':
            logging.error('Uploaded file is empty')
            return jsonify({'error': 'Uploaded file is empty'}), 400

        png_payment_bill = convert_to_png(payment_bill)
        png_proof_for_payment_bill = convert_to_png(proof_for_payment_bill)

        payment_text = extract_text_from_image(png_payment_bill)
        proof_text = extract_text_from_image(png_proof_for_payment_bill)

        if payment_text is not None and proof_text is not None:
            logging.debug(f"Payment Text: {payment_text}") # Log payment text
            logging.debug(f"Proof Text: {proof_text}") # Log proof text

            bill_details = extract_details(payment_text)
            proof_details = extract_details(proof_text)

            print(bill_details)
            print(proof_details)

            if bill_details['p_date'] == proof_details['p_date'] and \
            bill_details['p_dr_ac_no'] == proof_details['p_dr_ac_no'] and \
            bill_details['p_amt'] == proof_details['p_amt'] and \
            bill_details['p_cr_ac_no'] == proof_details['p_cr_ac_no']:
                passing_receipt_entry(bill_details)
                return jsonify({'message': 'Bill and proof details matched and entry passed.'})
            else:
                passing_receipt_entry(bill_details) # Add this line to record the entry even if details don't match
                return jsonify({'error': 'Bill and proof details do not match.'})
        return jsonify({"error": 'END'}), 400
    except Exception as e:
            return jsonify({'error': e}), 400
        
# Route for manual entry
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
        passing_receipt_entry(bill_details, is_manual=True)
        return jsonify({'message': 'Manual entry details matched and entry passed.'}), 200
    else:
        return jsonify({'error': 'Manual entry details do not match.'}), 400


@app.route('/')
def hello_world():
    return jsonify({
        "name": "Sparsh",
        "roll Number": "123" # Fixed the typo here
    })

if __name__ == '__main__':
    app.run(debug=True)
print("program done")