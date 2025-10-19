# Question: (Answers); Answers are in tuple format, so they can act as a key in a dictionary
# I think I abandoned that idea, though, so they probably don't need to be a tuple. I'm not gonna take the time to
# change that, though.
questions = {
    'Which design principle is demonstrated by separating public-facing servers in a DMZ from internal network '
    'resources?\n':
        ('Redundancy',
         'Defense in depth [DiD]',
         'Least privilege',
         'Segmentation'),

    'Which network design principle applies when implementing firewalls and intrusion detection systems [IDS]?\n':
        ('Accountability',
         'Least privilege',
         'Defense in depth [DiD]',
         'Separation of duties'),

    'Which principle is illustrated by requiring separate accounts for admin and user roles?\n':
        ('Adaptability',
         'Redundancy',
         'Separation of duties',
         'Defense in depth [DiD]'),

    'Which principle is implemented when configuring devices to only run necessary services?\n':
        ('Redundancy',
         'Minimization',
         'Isolation',
         'Accountability'),

    'Which action mitigates a denial-of-service (DoS) attack\n':
        ('Using data encryption',
         'Installing antivirus software',
         'Implementing multifactor authentication',
         'Limiting incoming traffic'),

    'An attacker installs malicious software on endpoints.\n\n'
    'Which solution prevents this?\n':
        ('Applying rate limiting',
         'Enforcing application safelisting',
         'Implementing encryption',
         'Using an intrusion prevention system [IPS]'),

    'What mitigates an attack involving spoofed email messages?\n':
        ('Firewalls',
         'Encryption',
         'Data backups',
         'Email filtering with domain authentication'),

    'Which solution addresses an attack that captures unencrypted data packets?\n':
        ('Maintaining data backups',
         'Implementing firewalls',
         'Deploying intrusion detection systems [IDS]',
         'Using encryption protocols [e.g., TLS]'),

    'Which method secures sensitive files stored on a server?\n':
        ('Applying rate limiting',
         'Using firewalls',
         'Deploying intrusion detection systems [IDS]',
         'Encrypting files at rest'),

    'How can a company secure an application against SQL injection attacks?\n':
        ('Network segmentation',
         'Data encryption',
         'Multifactor authentication',
         'Input validation'),

    'What secures data during transmission across public networks?\n':
        ('Intrusion prevention systems',
         'TLS encryption',
         'Data backups',
         'Firewalls'),

    'Which solution ensures application configurations remain secure?\n':
        ('Maintaining data backups',
         'Applying rate limiting',
         'Using configuration management tools',
         'Deploying firewalls'),

    'Which AAA category is involved when logs are analyzed to determine user actions?\n':
        ('Access control',
         'Authorization',
         'Accounting',
         'Authentication'),

    'Which AAA category involves verifying a user’s identity with a password?\n':
        ('Access control',
         'Authorization',
         'Accounting',
         'Authentication'),

    'Which AAA process limits a user’s access to specific files?\n':
        ('Identification',
         'Authorization',
         'Accounting',
         'Authentication'),

    'Which AAA function tracks user activities during a session?\n':
        ('Auditing',
         'Authorization',
         'Accounting',
         'Authentication'),

    'Which governance framework ensures a company complies with data protection laws?\n':
        ('Rate-limiting measures',
         'Access control policies',
         'Firewall rules',
         'Regulatory compliance policies'),

    'Which governance solution ensures changes to IT systems are reviewed and approved?\n':
        ('Intrusion detection systems',
         'Change management policies',
         'Backup plans',
         'Incident response plans'),

    'Which governance process ensures employees are trained in security protocols?\n':
        ('Firewall rules',
         'Security awareness training',
         'Incident response plans',
         'Regulatory compliance'),

    'Which governance solution establishes guidelines for data classification?\n':
        ('Incident response plans',
         'Firewall rules',
         'Change management policies',
         'Data classification policies'),
}

# In format of cq'n'_response create full response list in All_Tests module
responses = {
    'cq1_response':
        ['Try again. Redundancy ensures availability, not segmentation.',
         'Try again. Defense in depth (DiD) refers to using multiple layers of defense, not network separation.',
         'Try again. Least privilege restricts user access, not network traffic.',
         'That’s right! Segmentation involves separating parts of a network to reduce risk and exposure.'],

    'cq2_response':
        ['Try again. Accountability ensures actions can be tracked back to individuals or systems.',
         'Try again. Least privilege applies to restricting access rights, not layers of defense.',
         'That’s right! Defense in depth (DiD) uses multiple layers of security for greater protection.',
         'Try again. Separation of duties is about dividing responsibilities among individuals.'],

    'cq3_response':
        ['Try again. Adaptability is about adjusting defenses to evolving threats.',
         'Try again. Redundancy ensures availability, not division of duties.',
         'That’s right! Separation of duties prevents misuse of privileges by dividing responsibilities.',
         'Try again. Defense in depth (DiD) refers to multiple layers of protection, not separating roles.'],

    'cq4_response':
        ['Try again. Redundancy focuses on reliability, not reducing system exposure.',
         'That’s right! Minimization reduces the attack surface by disabling unnecessary services.',
         'Try again. Isolation involves segregating resources, not managing active services.',
         'Try again. Accountability tracks actions but does not reduce running services.'],

    'cq5_response':
        ['Try again. Encryption secures data but does not address traffic volume.',
         'Try again. Antivirus software prevents malware but does not address DoS attacks.',
         'Try again. Multifactor authentication secures accounts, not network traffic.',
         'That’s right! Limiting controls traffic volume and helps mitigate DoS attacks.'],

    'cq6_response':
        ['Try again. Rate limiting controls traffic volume but does not address software installation.',
         'That’s right! Application safelisting allows only approved programs to run, preventing unauthorized '
         'software.',
         'Try again. Encryption secures data, not software execution.',
         'Try again. IPS detects and blocks threats but does not limit software installation.'],

    'cq7_response':
        ['Try again. Firewalls manage network traffic but do not authenticate emails.',
         'Try again. Encryption secures communication but does not filter emails.',
         'Try again. Data backups restore lost data but do not prevent spoofed messages.',
         'That’s right! Email filtering and domain authentication identify and block spoofed emails.'],

    'cq8_response':
        ['Try again. Backups restore data but do not secure transmissions.',
         'Try again. Firewalls control traffic but do not encrypt data.',
         'Try again. IDS detects anomalies but does not encrypt communication.',
         'That’s right! Encryption protocols like TLS prevent packet capture by securing data in transit.'],

    'cq9_response':
        ['Try again. Rate limiting controls traffic but does not secure stored data.',
         'Try again. Firewalls protect networks but do not secure stored data.',
         'Try again. IDS monitors threats but does not encrypt files.',
         'That’s right! Encryption ensures stored data remains secure, even if accessed without authorization.'],

    'cq10_response':
        ['Try again. Segmentation divides networks but does not prevent SQL injection.',
         'Try again. Encryption secures data but does not validate input.',
         'Try again. Multifactor authentication secures accounts, not application inputs.',
         'That’s right! Input validation prevents malicious SQL commands from being executed.'],

    'cq11_response':
        ['Try again. IPS blocks threats but does not encrypt transmissions.',
         'That’s right! TLS encryption secures data during transmission.',
         'Try again. Backups protect stored data, not data in transit.',
         'Try again. Firewalls manage traffic but do not secure data in transit.'],

    'cq12_response':
        ['Try again. Backups restore data but do not manage configurations.',
         'Try again. Rate limiting controls traffic but does not manage configurations.',
         'That’s right! Configuration management tools monitor and secure application settings.',
         'Try again. Firewalls secure networks, not application configurations.'],

    'cq13_response':
        ['Try again. Access control manages permissions, not logs.',
         'Try again. Authorization manages permissions but does not track actions.',
         'That’s right! Accounting tracks user actions for auditing purposes.',
         'Try again. Authentication verifies identity but does not involve logging actions.'],

    'cq14_response':
        ['Try again. Access control defines permissions but does not verify identity.',
         'Try again. Authorization determines access rights after authentication.',
         'Try again. Accounting tracks user actions but does not verify identity.',
         'That’s right! Authentication verifies identity using credentials like passwords.'],

    'cq15_response':
        ['Try again. Identification identifies the user but does not limit file access.',
         'That’s right! Authorization determines what resources a user can access.',
         'Try again. Accounting tracks actions, not access rights.',
         'Try again. Authentication verifies identity, not access rights.'],

    'cq16_response':
        ['Try again. Auditing is a broader concept beyond the AAA framework.',
         'Try again. Authorization controls access but does not track activities.',
         'That’s right! Accounting logs user activities for auditing.',
         'Try again. Authentication verifies identity but does not track activities.'],

    'cq17_response':
        ['Try again. Rate limiting controls traffic but does not enforce governance.',
         'Try again. Access control policies manage access rights, not compliance.',
         'Try again. Firewall rules control network traffic but do not ensure compliance.',
         'That’s right! Regulatory compliance policies align operations with legal requirements.'],

    'cq18_response':
        ['Try again. IDS detects threats but does not manage system changes.',
         'That’s right! Change management policies ensure proper review and approval of IT changes.',
         'Try again. Backup plans protect data but do not govern IT changes.',
         'Try again. Incident response plans handle security events but do not manage system changes.'],

    'cq19_response':
        ['Try again. Firewall rules manage traffic but do not involve training.',
         'That’s right! Security awareness training ensures employees understand security protocols.',
         'Try again. Incident response plans address security events, not training.',
         'Try again. Regulatory compliance ensures adherence to laws but does not focus on employee training.'],

    'cq20_response':
        ['Try again. Incident response plans address events but do not classify data.',
         'Try again. Firewall rules manage traffic but do not classify data.',
         'Try again. Change management addresses IT changes, not data categorization.',
         'That’s right! Data classification policies define how data is categorized and secured.'],
}

quest_key_list = list(questions.keys())
resp_key_list = list(responses.keys())
