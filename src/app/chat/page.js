"use client";

import Link from 'next/link';
import { useRouter } from 'next/navigation';
import React, { useState } from 'react';


const FinancialBot = () => {
    const router = useRouter();
    // State to manage user's selected options
    const [selectedOption, setSelectedOption] = useState(null);

    // Function to handle user's selection
    const handleOptionSelect = (option) => {
        setSelectedOption(option);
    };


    const handleConfirmation = (choice) => {
        if (choice === 'no') {
            // Redirect to the home Page
            router.push('/');
        } else {
            // Handle other choices if necessary
        }
    };

    // Data structure for main options and follow-up options
    const options = {
        main: [
            'Uploading and Extracting Bill Data',
            'Internal Audit and Authentication',
            'Journal Entries and Accounting',
            'User Access and Roles',
            'AI Assistant',
            'General Questions',
            'Bill Information and Clarity',
            'E-bill Creation and Management',
            'Payment Processing',
            'System Functionality and Navigation',
            'Additional Features and Integrations'
        ],
        followUp: {
            'Uploading and Extracting Bill Data': [
                'What file formats are accepted for uploading bills?',
                'Does the system automatically extract all data from uploaded bills?',
                'How can errors in extracted data be corrected?'
            ],
            'Internal Audit and Authentication': [
                'What criteria are used by the internal audit to determine if a bill is legitimate?',
                'How are proofs used to authenticate bills (e.g., receipts, contracts)?',
                'What happens if a bill fails the internal audit?'
            ],
            'Journal Entries and Accounting': [
                'How does the system categorize and segregate journal entries for further audit?',
                'How are these journal entries used to update the general ledger and trial balance?',
                'Can the system automatically generate accounting reports based on the processed bills?'
            ],
            'User Access and Roles': [
                'What user roles are there in the system (e.g., admin, accountant)?',
                'What permissions does each user role have?',
                'How are users authenticated and authorized to access the system?'
            ],
            'AI Assistant': [
                'What specific tasks can the AI assistant help users with?',
                'How can users access the AI assistant?',
                'Is the AI assistant able to learn and improve over time?'
            ],
            'General Questions': [
                'What is the benefit of using this system for processing bills?',
                'How secure is the system for storing and handling financial data?',
                'Is there a cost associated with using this system?'
            ],
            'Bill Information and Clarity': [
                'Are there any limitations on the size or complexity of bills the system can handle?',
                'What happens if the bill lacks clear information or has blurry text?',
                'Can the system process handwritten bills?'
            ],
            'E-bill Creation and Management': [
                'How can users create e-bills within the system, if applicable?',
                'Can users schedule automatic e-bill delivery to specific recipients?',
                'Does the system offer functionalities for managing e-bill subscriptions?'
            ],
            'Payment Processing': [
                'Can users initiate bill payments through the system?',
                'If so, what payment methods are supported (e.g., bank transfer, credit card)?',
                'Does the system integrate with any external payment gateways?'
            ],
            'System Functionality and Navigation': [
                'Does the system offer search functions to locate specific bills easily?',
                'Can users set up filters or preferences to personalize their experience?',
                'Are there tutorials or help guides available for users unfamiliar with the system?'
            ],
            'Additional Features and Integrations': [
                'Does the system integrate with any accounting or financial management software?',
                'Can users export bill data in various formats (e.g., CSV, Excel)?',
                'Does the system offer any features for data analysis or reporting beyond basic accounting?'
            ]
        },
        answers: {
            'What file formats are accepted for uploading bills?': 'The system accepts PDF, JPG, and PNG file formats for uploading bills.',
            'Does the system automatically extract all data from uploaded bills?': 'Yes, the system automatically extracts key data such as date, debitor\'s account number, and amount using OCR technology.',
            'How can errors in extracted data be corrected?': 'Errors in extracted data can be corrected manually through the system interface.',
            'What criteria are used by the internal audit to determine if a bill is legitimate?': 'The internal audit uses various criteria such as consistency, authenticity of proofs, and compliance with predefined rules to determine the legitimacy of a bill.',
            'How are proofs used to authenticate bills (e.g., receipts, contracts)?': 'Proofs such as receipts and contracts are used to verify the authenticity and validity of bills during the authentication process.',
            'What happens if a bill fails the internal audit?': 'If a bill fails the internal audit, it is flagged as suspicious and segregated for further investigation and resolution by authorized personnel.',
            'How does the system categorize and segregate journal entries for further audit?': 'The system categorizes journal entries based on their nature and risk profile, segregating them into suspicious, normal, and manual folders for easy auditing and resolution.',
            'How are these journal entries used to update the general ledger and trial balance?': 'Journal entries are used to update the general ledger and trial balance, ensuring accurate and up-to-date financial records.',
            'Can the system automatically generate accounting reports based on the processed bills?': 'Yes, the system can automatically generate accounting reports based on the processed bills, providing comprehensive insights into financial transactions and performance.',
            'What user roles are there in the system (e.g., admin, accountant)?': 'The system supports various user roles such as admin, accountant, and auditor, each with specific permissions and access levels.',
            'What permissions does each user role have?': 'Admins have full control over system settings and user management, accountants can manage bills and financial data, and auditors can review and audit transactions.',
            'How are users authenticated and authorized to access the system?': 'Users are authenticated using secure login credentials, and their access rights are determined by their assigned roles and permissions within the system.',
            'What specific tasks can the AI assistant help users with?': 'The AI assistant can help users with tasks such as bill processing, journal entry generation, internal audits, and providing assistance and guidance through the chat interface.',
            'How can users access the AI assistant?': 'Users can access the AI assistant through the help section of the system interface, where they can initiate conversations and seek assistance for their queries and tasks.',
            'Is the AI assistant able to learn and improve over time?': 'Yes, the AI assistant is designed to learn from user interactions and feedback, continuously improving its capabilities and accuracy over time.',
            'What is the benefit of using this system for processing bills?': 'The system streamlines bill processing tasks, reduces manual effort, ensures accuracy in data extraction, and provides comprehensive audit trails for compliance and transparency.',
            'How secure is the system for storing and handling financial data?': 'The system employs robust security measures such as encryption, access controls, and regular audits to ensure the security and confidentiality of financial data.',
            'Is there a cost associated with using this system?': 'Yes, there may be a subscription or licensing fee associated with using the system, depending on the selected plan and features.',
            'Are there any limitations on the size or complexity of bills the system can handle?': 'The system is capable of handling bills of various sizes and complexity, with no specific limitations mentioned.',
            'What happens if the bill lacks clear information or has blurry text?': 'If a bill lacks clear information or has blurry text, users may need to manually input or correct the data to ensure accuracy in processing.',
            'Can the system process handwritten bills?': 'Yes, the system is designed to process handwritten bills using advanced OCR (Optical Character Recognition) technology.',
            'How can users create e-bills within the system, if applicable?': 'Users can create e-bills within the system by entering the required details manually or importing electronic invoices in supported formats.',
            'Can users schedule automatic e-bill delivery to specific recipients?': 'Yes, users can schedule automatic e-bill delivery to specific recipients, ensuring timely and efficient invoicing processes.',
            'Does the system offer functionalities for managing e-bill subscriptions?': 'Yes, the system offers functionalities for managing e-bill subscriptions, allowing users to track, update, and customize their subscription preferences.',
            'Can users initiate bill payments through the system?': 'Yes, users can initiate bill payments through the system, facilitating seamless and efficient transaction processing.',
            'If so, what payment methods are supported (e.g., bank transfer, credit card)?': 'The system supports various payment methods such as bank transfers, credit cards, and other electronic payment options, depending on the configured settings and integrations.',
            'Does the system integrate with any external payment gateways?': 'Yes, the system integrates with external payment gateways to facilitate secure and reliable transaction processing, offering flexibility and convenience to users.',
            'Does the system offer search functions to locate specific bills easily?': 'Yes, the system offers search functions to locate specific bills easily, enabling users to quickly retrieve and access relevant financial data as needed.',
            'Can users set up filters or preferences to personalize their experience?': 'Yes, users can set up filters or preferences to personalize their experience, allowing them to customize their workflow and interface settings according to their preferences and requirements.',
            'Are there tutorials or help guides available for users unfamiliar with the system?': 'Yes, there are tutorials and help guides available within the system interface to assist users in getting started and mastering its functionalities.',
            'Does the system integrate with any accounting or financial management software?': 'Yes, the system integrates with various accounting or financial management software, enabling seamless data exchange and interoperability for enhanced productivity and efficiency.',
            'Can users export bill data in various formats (e.g., CSV, Excel)?': 'Yes, users can export bill data in various formats such as CSV, Excel, and PDF, providing flexibility in data analysis and reporting.',
            'Does the system offer any features for data analysis or reporting beyond basic accounting?': 'Yes, the system offers advanced features for data analysis and reporting beyond basic accounting functionalities, empowering users with insights and intelligence for informed decision-making.'
        }
    };

    return (
        <>
            <nav class="bg-[#2C1E4A] h-12 text-end text-sm fixed w-full text-white top-0 z-10 py-4 px-5">
                <ul class="flex gap-8 justify-end">
                    <li><Link href={"/"}>Home</Link></li>
                    <li><Link href={"/bill"}>Bills</Link></li>
                    <li><Link href={"/audit"}>Audit</Link></li>
                    <li><Link href={"/chat"}>FAQs</Link></li>
                    <li><Link href={"/chat"}>Help</Link></li>
                    <li><Link href={"/view"}>View</Link></li>
                </ul>
            </nav>
            <div className="container mx-auto p-4">
                {selectedOption === null ? (
                    <div>
                        <h3 className="text-lg font-semibold mb-4">Please select an option:</h3>
                        <ul className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
                            {options.main.map((option, index) => (
                                <li key={index} className="border border-gray-200 rounded p-4 cursor-pointer hover:bg-gray-100 transition duration-300" onClick={() => handleOptionSelect(option)}>
                                    {option}
                                </li>
                            ))}
                        </ul>
                    </div>
                ) : (
                    <div>
                        <h3 className="text-lg font-semibold mb-4">{selectedOption}</h3>
                        <ul>
                            {options.followUp[selectedOption].map((question, index) => (
                                <li key={index} className="mb-4">
                                    <p className="mb-2">{question}</p>
                                    <p className="font-semibold">{options.answers[question]}</p>
                                </li>
                            ))}
                        </ul>
                        <div className="mt-4">
                            <button
                                className="bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded mr-2"
                                onClick={() => handleConfirmation('okay')}
                            >
                                Okay, I got it. Thanks!
                            </button>
                            <button
                                className="bg-red-500 hover:bg-red-600 text-white font-semibold py-2 px-4 rounded"
                                onClick={() => handleConfirmation('no')}
                            >
                                No, I need personalized help
                            </button>
                        </div>
                    </div>
                )}
            </div>
        </>
    );
};

export default FinancialBot;
