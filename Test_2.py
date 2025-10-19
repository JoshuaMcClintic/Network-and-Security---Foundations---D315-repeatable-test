# Question: (Answers); Answers are in tuple format, so they can act as a key in a dictionary
# I think I abandoned that idea, though, so they probably don't need to be a tuple. I'm not gonna take the time to
# change that, though.
questions = {
    'An attacker initiates a distributed denial-of-service (DDoS) attack on a corporate web server.\n\n'
    'Which type of risk is being exploited?\n':
        ('Integrity risk',
         'Confidentiality risk',
         'Non-repudiation risk',
         'Availability risk'),

    'A company’s IT department discovers malware that is logging keystrokes and transmitting them to an external '
    'server.\n\n'
    'Which threat type describes this situation?\n':
        ('Data exfiltration',
         'Social engineering',
         'Denial of service',
         'Phishing'),

    'Which situation is classified as a physical security risk to a network?\n':
        ('Malware infection',
         'Phishing attempt',
         'Data breach',
         'Power outage'),

    'An attacker uses an organization’s poorly secured Wi-Fi network to access internal resources.\n\n'
    'Which term describes the Wi-Fi network in this scenario?\n':
        ('Asset',
         'Threat',
         'Countermeasure',
         'Vulnerability'),

    'A user receives an email impersonating the IT department and asking for login credentials.\n\n'
    'Which type of threat is this?\n':
        ('Trojan',
         'Phishing',
         'Keylogger',
         'Worm'),

    'A network scan reveals that a company’s database server is running outdated software with known '
    'vulnerabilities.\n\n'
    'Which type of risk does this scenario describe?\n':
        ('Insider',
         'Threat',
         'Physical',
         'Vulnerability'),

    'An attacker intercepts unencrypted data being transmitted over a network.\n\n'
    'What is the attacker exploiting in this scenario?\n':
        ('Data integrity',
         'Data authentication',
         'Data confidentiality',
         'Data availability'),

    'Which situation is an example of a social engineering attack?\n':
        ('A brute-force password-cracking attempt',
         'Malware infecting a corporate server',
         'A distributed denial-of-service (DDoS) attack',
         'A phishing email requesting login credentials'),

    'Employees use personal devices to access the corporate network without adequate security measures.\n\n'
    'Which type of risk does this pose?\n':
        ('Integrity',
         'BYOD',
         'External threat',
         'Insider threat'),

    'A company uses a firewall to block unauthorized traffic from reaching its internal network.\n\n'
    'Which role does the firewall serve in this scenario?\n':
        ('Safeguard',
         'Countermeasure',
         'Threat',
         'Vulnerability'),

    'Which aspect of the CIA triad is addressed by encrypting sensitive emails before transmission to ensure only the '
    'intended recipient can read them?\n':
        ('Non-repudiation',
         'Integrity',
         'Availability',
         'Confidentiality'),

    'A hospital implements digital signatures to verify that electronic health records are not altered during '
    'transmission.\n\n'
    'Which part of the CIA triad does this action address?\n':
        ('Authentication',
         'Integrity',
         'Availability',
         'Confidentiality'),

    'A disaster recovery system is installed to ensure that data can be quickly restored in case of a failure.\n\n'
    'Which part of the CIA triad does this primarily address?\n':
        ('Authenticity',
         'Integrity',
         'Availability',
         'Confidentiality'),

    'Which aspect of the CIA triad is addressed by restricting access to sensitive customer information using '
    'role-based access control?\n':
        ('Authentication',
         'Integrity',
         'Availability',
         'Confidentiality'),

    'A software development company employs hash functions to ensure that code deployed to clients has not been '
    'tampered with.\n\n'
    'Which category of the CIA triad is this ensuring?\n':
        ('Non-repudiation',
         'Integrity',
         'Availability',
         'Confidentiality'),

    'An organization deploys multifactor authentication (MFA) to ensure only authorized users can log in to its '
    'systems.\n\n'
    'Which CIA triad component does this primarily support?\n':
        ('Authentication',
         'Confidentiality',
         'Availability',
         'Integrity'),

    'A company schedules regular backups of its critical systems to mitigate the impact of hardware failure.\n\n'
    'Which CIA triad component does this action support?\n':
        ('Availability',
         'Non-repudiation',
         'Confidentiality',
         'Integrity'),

    'An organization has decided to encrypt sensitive emails before sending them, ensuring only the intended recipient '
    'can read their contents.\n\n'
    'Which aspect of the CIA triad does this practice address?\n':
        ('Non-repudiation',
         'Integrity',
         'Availability',
         'Confidentiality'),

    'A bank employs a hashing algorithm to verify that transaction logs have not been altered.\n\n'
    'Which CIA triad category does this measure support?\n':
        ('Authentication',
         'Integrity',
         'Availability',
         'Confidentiality'),

    'A government agency ensures that emergency response systems are operational 24/7 to guarantee service access '
    'during a crisis.\n\n'
    'Which CIA triad component does this support?\n':
        ('Non-repudiation',
         'Integrity',
         'Availability',
         'Confidentiality'),
}

# In format of bq'n'_response create full response list in All_Tests module
responses = {
    'bq1_response':
        ['Try again. Integrity risk involves unauthorized changes to data. Here, the attacker aims to disrupt access, '
         'not alter data.',
         'Try again. Confidentiality risk refers to risks that could expose sensitive data to unauthorized access. '
         'This scenario does not involve exposure of data.',
         'Try again. Non-repudiation risk relates to the ability to verify actions or messages. This scenario focuses '
         'on access disruption.',
         'That’s right! Availability risk affects the ability to access resources. A DDoS attack is designed to make '
         'the web server unavailable.'],

    'bq2_response':
        ['That’s right! Data exfiltration involves unauthorized data transmission, such as keystrokes, to an external '
         'server.',
         'Try again. Social engineering manipulates individuals to gain unauthorized access or information, often '
         'without malware.',
         'Try again. Denial of service aims to disrupt access, not capture and transmit information.',
         'Try again. Phishing involves misleading users into providing sensitive information but does not usually '
         'involve malware.'],

    'bq3_response':
        ['Try again. Malware is a software-based risk, not a physical security risk.',
         'Try again. Phishing is an attempt to gain information through social manipulation, not a physical security '
         'risk.',
         'Try again. Data breaches usually refer to unauthorized data access rather than physical security risks.',
         'That’s right! A power outage is a physical security risk that can interrupt network functionality.'],

    'bq4_response':
        ['Try again. An asset is something valuable that needs protection, not a weakness.',
         'Try again. The threat here would be the attacker exploiting the network.',
         'Try again. A countermeasure is a security control that reduces risk, not a weakness.',
         'That’s right! A vulnerability is a weakness that allows threats to exploit a system, as in the case of '
         'poorly secured Wi-Fi.'],

    'bq5_response':
        ['Try again. A Trojan is malware that appears legitimate but performs malicious actions.',
         'That’s right! Phishing involves deceptive communication to gather sensitive information like login '
         'credentials.',
         'Try again. A keylogger is malware that records keystrokes but is not involved in tricking users into '
         'providing information.',
         'Try again. A worm is a type of self-replicating malware, not a method to capture login information.'],

    'bq6_response':
        ['Try again. Insider risks involve employees or insiders, which is not the focus here.',
         'Try again. A threat is an external factor, such as a hacker, that could exploit vulnerabilities, but this '
         'scenario identifies the weakness itself.',
         'Try again. Physical risks are associated with tangible elements, like hardware damage, not software '
         'weaknesses.',
         'That’s right! A vulnerability risk refers to weaknesses in systems or software that could be exploited.'],

    'bq7_response':
        ['Try again. Integrity involves protecting data from being modified, which is not the attacker’s action here.',
         'Try again. Authentication verifies identities or actions but is not related to data interception.',
         'That’s right! Data confidentiality is compromised when unauthorized parties intercept sensitive information.',
         'Try again. Availability refers to ensuring access to resources, which is not the concern in this scenario.'],

    'bq8_response':
        ['Try again. Brute-force attacks rely on systematic password guessing rather than exploiting human behavior.',
         'Try again. Malware infection is a technical attack, not a social engineering tactic.',
         'Try again. A DDoS attack disrupts access to systems but does not involve manipulating individuals.',
         'That’s right! Phishing is a social engineering attack that manipulates individuals into revealing sensitive '
         'information.'],

    'bq9_response':
        ['Try again. Integrity risk involves unauthorized changes to data and not using insecure devices.',
         'That’s right! The risk of bringing your own device (BYOD) arises when personal devices introduce potential '
         'vulnerabilities or lack security controls.',
         'Try again. External threats come from outside the organization, while this risk originates within.',
         'Try again. Insider threats involve intentional, malicious activity by employees, which is not the focus '
         'here.'],

    'bq10_response':
        ['That’s right! A safeguard is a security control implemented to prevent risks like unauthorized access.',
         'Try again. A countermeasure is any action or system that mitigates risk, but this does not accurately '
         'describe what a firewall is.',
         'Try again. A threat is a potential danger, such as an attacker, which the firewall is protecting against.',
         'Try again. Vulnerabilities are weaknesses that could be exploited, while a firewall is designed to protect '
         'against them.'],

    'bq11_response':
        ['Try again. Non-repudiation ensures accountability for actions, which is not addressed by encryption.',
         'Try again. Integrity ensures data is not modified without authorization; encryption is primarily for '
         'confidentiality.',
         'Try again. Availability ensures resources are accessible when needed but does not protect sensitive data '
         'from unauthorized access.',
         'That’s right! Confidentiality ensures that information is protected from unauthorized access, and encryption '
         'is a key method of achieving this.'],

    'bq12_response':
        ['Try again. Authentication ensures users are who they claim to be, but this scenario focuses on protecting '
         'data accuracy.',
         'That’s right! Integrity ensures data remains accurate and unaltered; digital signatures help verify this.',
         'Try again. Availability ensures data is accessible when needed, which is unrelated to verifying unaltered '
         'data.',
         'Try again. Confidentiality ensures unauthorized users cannot access data, while digital signatures address '
         'data integrity.'],

    'bq13_response':
        ['Try again. Authenticity verifies the origin or legitimacy of users or systems, which is not addressed by '
         'disaster recovery.',
         'Try again. Integrity ensures that data is accurate and unmodified, but disaster recovery ensures '
         'accessibility after a failure.',
         'That’s right! Availability ensures resources remain accessible, and disaster recovery systems help achieve '
         'this.',
         'Try again. Confidentiality protects data from unauthorized access, while disaster recovery focuses on '
         'availability.'],

    'bq14_response':
        ['Try again. Authentication verifies the identity of users, but access control aligns with confidentiality.',
         'Try again. Integrity ensures data remains accurate and unaltered, which is not directly related to access '
         'control.',
         'Try again. Availability ensures access to resources when needed, which is not the focus of restricting '
         'access.',
         'That’s right! Role-based access control protects sensitive information from unauthorized access, ensuring '
         'confidentiality.'],

    'bq15_response':
        ['Try again. Non-repudiation addresses accountability, not data accuracy.',
         'That’s right! Integrity ensures data remains unaltered, and hash functions are a method to verify data '
         'authenticity.',
         'Try again. Availability ensures access to data and systems, not the accuracy of transmitted data.',
         'Try again. Confidentiality involves protecting data from unauthorized access, not verifying its accuracy.'],

    'bq16_response':
        ['Try again. While MFA is an authentication method, it primarily supports confidentiality by protecting access '
         'to sensitive information.',
         'That’s right! Confidentiality protects data from unauthorized access, which MFA supports by requiring '
         'additional verification.',
         'Try again. Availability focuses on ensuring access to resources, not preventing unauthorized access.',
         'Try again. Integrity involves maintaining accurate data, while MFA ensures only authorized users access '
         'data.'],

    'bq17_response':
        ['That’s right! Availability ensures resources remain accessible, and backups are key to maintaining '
         'availability.',
         'Try again. Non-repudiation addresses accountability, which is not relevant in this scenario.',
         'Try again. Confidentiality prevents unauthorized access, not ensuring data availability.',
         'Try again. Integrity ensures data accuracy, but regular backups focus on ensuring data accessibility after '
         'hardware failures.'],

    'bq18_response':
        ['Try again. Non-repudiation ensures accountability, which encryption for transmission security does not '
         'address.',
         'Try again. Integrity ensures data remains unaltered, which encryption does not directly address.',
         'Try again. Availability ensures data accessibility, not protecting it from unauthorized viewing.',
         'That’s right! Encrypting data ensures confidentiality by protecting it from unauthorized access.'],

    'bq19_response':
        ['Try again. Authentication verifies identity, not data consistency.',
         'That’s right! Integrity ensures data is accurate and unaltered, which is the purpose of hashing algorithms.',
         'Try again. Availability ensures resources are accessible; it does not focus on data accuracy.',
         'Try again. Confidentiality involves protecting data from unauthorized access, not verifying its accuracy.'],

    'bq20_response':
        ['Try again. Non-repudiation involves accountability, not ensuring service access.',
         'Try again. Integrity focuses on data accuracy, not operational readiness.',
         'That’s right! Availability ensures that resources are accessible when needed, which is critical during '
         'emergencies.',
         'Try again. Confidentiality involves protecting sensitive data, not ensuring system access.'],
}

quest_key_list = list(questions.keys())
resp_key_list = list(responses.keys())
