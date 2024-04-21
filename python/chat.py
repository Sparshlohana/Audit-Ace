import React, { useState } from 'react';

const FinancialBot = () => {
  // State to manage user's selected options
  const [selectedOption, setSelectedOption] = useState(null);

  // Function to handle user's selection
  const handleOptionSelect = (option) => {
    setSelectedOption(option);
  };

  // Function to handle user's confirmation or need for personalized help
  const handleConfirmation = (confirmation) => {
    if (confirmation === 'okay') {
      // User confirms understanding
      // Display farewell message or redirect to another page
    } else if (confirmation === 'no') {
      // User needs personalized help
      // Display contact information or initiate chat with support
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
    }
  };

  return (
    <div>
      {selectedOption === null ? (
        // Display main options if no option is selected
        <div>
          <h3>Please select an option:</h3>
          <ul>
            {options.main.map((option, index) => (
              <li key={index} onClick={() => handleOptionSelect(option)}>
                {option}
              </li>
            ))}
          </ul>
        </div>
      ) : (
        // Display follow-up options if an option is selected
        <div>
          <h3>{selectedOption}</h3>
          <ul>
            {options.followUp[selectedOption].map((question, index) => (
              <li key={index}>{question}</li>
            ))}
          </ul>
          <div>
            <button onClick={() => handleConfirmation('okay')}>Okay, I got it. Thanks!</button>
            <button onClick={() => handleConfirmation('no')}>No, I need personalized help</button>
          </div>
        </div>
      )}
    </div>
  );
};

export default FinancialBot;
