import copy
import random
import re


YEAR_1_PAPER = {
    "paper_title": "Year 1 Foundation Assessment",
    "sections": [
        {
            "id": "section_a",
            "title": "Section A: MCQs",
            "question_type": "mcq",
            "marks_per_question": 2,
            "questions": [
                {"id": "Y1A1", "question": "What does CPU stand for?", "options": ["Central Processing Unit", "Computer Power Unit", "Central Program Utility", "Control Processing User"], "answer": "Central Processing Unit", "explanation": "The CPU is the main processor that executes instructions."},
                {"id": "Y1A2", "question": "Which binary value is equal to decimal 10?", "options": ["1010", "1110", "1001", "1100"], "answer": "1010", "explanation": "Binary 1010 equals 8 + 2, which is 10."},
                {"id": "Y1A3", "question": "Which Python keyword is used to define a function?", "options": ["def", "func", "define", "lambda"], "answer": "def", "explanation": "Python functions are declared with the def keyword."},
                {"id": "Y1A4", "question": "Which memory loses its data when the power is turned off?", "options": ["RAM", "ROM", "SSD", "Cache disk"], "answer": "RAM", "explanation": "RAM is volatile memory and loses data without power."},
                {"id": "Y1A5", "question": "HTML is mainly used to create the ____ of a web page.", "options": ["structure", "sound", "database", "encryption"], "answer": "structure", "explanation": "HTML defines the structure and content of a web page."},
                {"id": "Y1A6", "question": "Which loop checks its condition before each iteration?", "options": ["while loop", "do while loop", "switch", "case loop"], "answer": "while loop", "explanation": "A while loop evaluates its condition before the loop body runs."},
                {"id": "Y1A7", "question": "Which Python data type is used for whole numbers?", "options": ["int", "float", "str", "list"], "answer": "int", "explanation": "The int type stores integer values."},
                {"id": "Y1A8", "question": "Which keyboard shortcut is commonly used to save a file?", "options": ["Ctrl+S", "Ctrl+P", "Ctrl+N", "Ctrl+L"], "answer": "Ctrl+S", "explanation": "Ctrl+S is the common save shortcut in most applications."},
                {"id": "Y1A9", "question": "A compiler converts source code into ____ code.", "options": ["machine", "binary search", "markup", "spreadsheet"], "answer": "machine", "explanation": "Compilers translate source code into machine-readable instructions."},
                {"id": "Y1A10", "question": "Which device is used to display output visually?", "options": ["Monitor", "Keyboard", "Scanner", "Microphone"], "answer": "Monitor", "explanation": "A monitor is an output device that displays information."}
            ]
        },
        {
            "id": "section_b",
            "title": "Section B: True or False",
            "question_type": "true_false",
            "marks_per_question": 2,
            "questions": [
                {"id": "Y1B1", "question": "A monitor is an output device.", "options": ["True", "False"], "answer": "True", "explanation": "A monitor shows output from the computer."},
                {"id": "Y1B2", "question": "An algorithm should have an infinite number of steps.", "options": ["True", "False"], "answer": "False", "explanation": "A valid algorithm must finish in a finite number of steps."},
                {"id": "Y1B3", "question": "Python lists are immutable.", "options": ["True", "False"], "answer": "False", "explanation": "Python lists are mutable and can be changed."},
                {"id": "Y1B4", "question": "One kilobyte is commonly treated as 1024 bytes.", "options": ["True", "False"], "answer": "True", "explanation": "In computing, 1 KB is often represented as 1024 bytes."},
                {"id": "Y1B5", "question": "Comments in a program are executed as instructions.", "options": ["True", "False"], "answer": "False", "explanation": "Comments are ignored during execution."},
                {"id": "Y1B6", "question": "LAN stands for a network that covers a small local area.", "options": ["True", "False"], "answer": "True", "explanation": "A Local Area Network connects devices in a limited area."},
                {"id": "Y1B7", "question": "A URL identifies a resource on the web.", "options": ["True", "False"], "answer": "True", "explanation": "A URL gives the address of a web resource."},
                {"id": "Y1B8", "question": "An SSD stores data using rotating magnetic platters.", "options": ["True", "False"], "answer": "False", "explanation": "SSDs use flash memory and have no spinning platters."},
                {"id": "Y1B9", "question": "In many programming languages, = is used for assignment.", "options": ["True", "False"], "answer": "True", "explanation": "A single equals sign typically assigns a value."},
                {"id": "Y1B10", "question": "The decimal number system has base 10.", "options": ["True", "False"], "answer": "True", "explanation": "Decimal numbers use ten digits from 0 to 9."}
            ]
        },
        {
            "id": "section_c",
            "title": "Section C: Fill in the Blanks",
            "question_type": "fill_blank",
            "marks_per_question": 1,
            "questions": [
                {"id": "Y1C1", "question": "The binary number system uses base ____.", "answer": "2", "explanation": "Binary uses only the digits 0 and 1, so its base is 2."},
                {"id": "Y1C2", "question": "The Python command used to display output is ____.", "answer": "print", "explanation": "The print function sends output to the screen."},
                {"id": "Y1C3", "question": "Temporary values while a program is running are stored in ____.", "answer": "memory", "explanation": "Running data is stored in memory."},
                {"id": "Y1C4", "question": "The pointing device used to click icons is a ____.", "answer": "mouse", "explanation": "A mouse is the standard pointing device."},
                {"id": "Y1C5", "question": "The file extension for a standard web page is ____.", "answer": "html", "explanation": "HTML files usually use the .html extension."},
                {"id": "Y1C6", "question": "A mistake in a program is called a ____.", "answer": "bug", "explanation": "Software errors are commonly called bugs."},
                {"id": "Y1C7", "question": "A set of instructions written for a computer is a ____.", "answer": "program", "explanation": "A program is a sequence of instructions for a computer."},
                {"id": "Y1C8", "question": "Software used to detect harmful code is called ____ software.", "answer": "antivirus", "explanation": "Antivirus software helps block malicious programs."},
                {"id": "Y1C9", "question": "The physical parts of a computer are called ____.", "answer": "hardware", "explanation": "Hardware refers to tangible computer components."},
                {"id": "Y1C10", "question": "The small icon for a website in a browser tab is often called a ____.", "answer": "favicon", "explanation": "A favicon is the small icon associated with a site."}
            ]
        }
    ]
}
YEAR_2_PAPER = {
    "paper_title": "Year 2 Programming and Data Structures Assessment",
    "sections": [
        {
            "id": "section_a",
            "title": "Section A: MCQs",
            "question_type": "mcq",
            "marks_per_question": 2,
            "questions": [
                {"id": "Y2A1", "question": "Which data structure follows FIFO order?", "options": ["Queue", "Stack", "Tree", "Graph"], "answer": "Queue", "explanation": "FIFO means first in, first out, which defines a queue."},
                {"id": "Y2A2", "question": "What is the time complexity of binary search on a sorted array?", "options": ["O(log n)", "O(n)", "O(n log n)", "O(1)"], "answer": "O(log n)", "explanation": "Binary search halves the search space each step."},
                {"id": "Y2A3", "question": "In object-oriented programming, a class is a ____ for creating objects.", "options": ["blueprint", "compiler", "database", "queue"], "answer": "blueprint", "explanation": "A class defines the structure and behavior of objects."},
                {"id": "Y2A4", "question": "Which stack operation removes the top element?", "options": ["pop", "push", "peek", "insert"], "answer": "pop", "explanation": "Pop removes the item from the top of the stack."},
                {"id": "Y2A5", "question": "Insertion at the beginning of a linked list usually takes ____ time.", "options": ["O(1)", "O(n)", "O(log n)", "O(n log n)"], "answer": "O(1)", "explanation": "Updating the head pointer is a constant-time operation."},
                {"id": "Y2A6", "question": "Recursion happens when a function ____.", "options": ["calls itself", "deletes itself", "sorts a queue", "creates a database"], "answer": "calls itself", "explanation": "A recursive function solves a problem by calling itself."},
                {"id": "Y2A7", "question": "Which technique is commonly used for very fast key-based lookup?", "options": ["Hashing", "Bubble sort", "Recursion", "Traversal only"], "answer": "Hashing", "explanation": "Hashing maps keys to locations for quick access."},
                {"id": "Y2A8", "question": "A tree node with at most two children belongs to a ____ tree.", "options": ["binary", "ternary", "linear", "cyclic"], "answer": "binary", "explanation": "A binary tree allows at most two children per node."},
                {"id": "Y2A9", "question": "Which OOP principle hides internal implementation details from the user?", "options": ["Encapsulation", "Inheritance", "Iteration", "Compilation"], "answer": "Encapsulation", "explanation": "Encapsulation hides internal details while exposing controlled access."},
                {"id": "Y2A10", "question": "Which algorithm repeatedly compares adjacent elements and swaps them if needed?", "options": ["Bubble sort", "Binary search", "Hashing", "DFS"], "answer": "Bubble sort", "explanation": "Bubble sort works through repeated adjacent swaps."}
            ]
        },
        {
            "id": "section_b",
            "title": "Section B: True or False",
            "question_type": "true_false",
            "marks_per_question": 2,
            "questions": [
                {"id": "Y2B1", "question": "Array elements are usually stored in contiguous memory locations.", "options": ["True", "False"], "answer": "True", "explanation": "Arrays reserve continuous memory for indexed access."},
                {"id": "Y2B2", "question": "A queue follows the LIFO principle.", "options": ["True", "False"], "answer": "False", "explanation": "A queue follows FIFO, not LIFO."},
                {"id": "Y2B3", "question": "An object is an instance of a class.", "options": ["True", "False"], "answer": "True", "explanation": "Objects are created from class definitions."},
                {"id": "Y2B4", "question": "Merge sort has a worst-case time complexity of O(n^2).", "options": ["True", "False"], "answer": "False", "explanation": "Merge sort runs in O(n log n) time."},
                {"id": "Y2B5", "question": "The function call stack helps manage recursive function execution.", "options": ["True", "False"], "answer": "True", "explanation": "Every recursive call adds a new frame to the call stack."},
                {"id": "Y2B6", "question": "A doubly linked list stores references to both previous and next nodes.", "options": ["True", "False"], "answer": "True", "explanation": "Doubly linked lists move in both directions."},
                {"id": "Y2B7", "question": "Polymorphism allows one interface to represent many forms.", "options": ["True", "False"], "answer": "True", "explanation": "Polymorphism lets different objects respond through a common interface."},
                {"id": "Y2B8", "question": "Binary search works correctly on an unsorted array.", "options": ["True", "False"], "answer": "False", "explanation": "Binary search requires sorted data."},
                {"id": "Y2B9", "question": "Constructors are commonly used to initialize objects.", "options": ["True", "False"], "answer": "True", "explanation": "Constructors set up an object's starting state."},
                {"id": "Y2B10", "question": "A graph can contain cycles.", "options": ["True", "False"], "answer": "True", "explanation": "Graphs can include paths that loop back to earlier nodes."}
            ]
        },
        {
            "id": "section_c",
            "title": "Section C: Fill in the Blanks",
            "question_type": "fill_blank",
            "marks_per_question": 1,
            "questions": [
                {"id": "Y2C1", "question": "In a stack, insertion is called ____.", "answer": "push", "explanation": "Push places a new item on top of the stack."},
                {"id": "Y2C2", "question": "In a queue, deletion is called ____.", "answer": "dequeue", "explanation": "Dequeue removes an item from the front of the queue."},
                {"id": "Y2C3", "question": "A tree node with no children is called a ____ node.", "answer": "leaf", "explanation": "Leaf nodes appear at the ends of tree branches."},
                {"id": "Y2C4", "question": "The efficiency of an algorithm is often measured by its time ____.", "answer": "complexity", "explanation": "Time complexity describes how running time grows with input size."},
                {"id": "Y2C5", "question": "Data hiding in OOP is achieved using ____.", "answer": "encapsulation", "explanation": "Encapsulation hides internal state behind methods."},
                {"id": "Y2C6", "question": "A linked ____ stores elements through nodes connected by references.", "answer": "list", "explanation": "A linked list connects nodes using references."},
                {"id": "Y2C7", "question": "The first valid index in many programming languages is ____.", "answer": "0", "explanation": "Most common languages use zero-based indexing."},
                {"id": "Y2C8", "question": "A recursive algorithm must have a base ____.", "answer": "case", "explanation": "The base case stops recursion."},
                {"id": "Y2C9", "question": "In a binary tree, each node has at most ____ children.", "answer": "2", "explanation": "Binary trees allow no more than two children per node."},
                {"id": "Y2C10", "question": "A collection of key-value pairs in Python is called a ____.", "answer": "dictionary", "explanation": "Python dictionaries map keys to values."}
            ]
        }
    ]
}
YEAR_3_PAPER = {
    "paper_title": "Year 3 Systems and Database Assessment",
    "sections": [
        {
            "id": "section_a",
            "title": "Section A: MCQs",
            "question_type": "mcq",
            "marks_per_question": 2,
            "questions": [
                {"id": "Y3A1", "question": "Which database concept helps reduce redundant data?", "options": ["Normalization", "Fragmentation", "Encapsulation", "Compilation"], "answer": "Normalization", "explanation": "Normalization organizes tables to reduce redundancy."},
                {"id": "Y3A2", "question": "Which key uniquely identifies each row in a table?", "options": ["Primary key", "Foreign key", "Candidate pointer", "Index column"], "answer": "Primary key", "explanation": "A primary key uniquely identifies every record."},
                {"id": "Y3A3", "question": "Which operating system component selects the next process to run?", "options": ["Scheduler", "Compiler", "Assembler", "Loader"], "answer": "Scheduler", "explanation": "The scheduler chooses which process gets CPU time next."},
                {"id": "Y3A4", "question": "Which protocol is commonly used for secure web browsing?", "options": ["HTTPS", "FTP", "SMTP", "Telnet"], "answer": "HTTPS", "explanation": "HTTPS protects web traffic with encryption."},
                {"id": "Y3A5", "question": "DNS is used to translate domain names into ____ addresses.", "options": ["IP", "MAC", "RAM", "USB"], "answer": "IP", "explanation": "DNS maps names like example.com to IP addresses."},
                {"id": "Y3A6", "question": "Which protocol is connectionless?", "options": ["UDP", "TCP", "HTTPS", "SSH"], "answer": "UDP", "explanation": "UDP sends packets without first creating a connection."},
                {"id": "Y3A7", "question": "Which SQL operation combines rows from two or more tables?", "options": ["JOIN", "DROP", "DELETE", "ROLLBACK"], "answer": "JOIN", "explanation": "JOIN merges related data from multiple tables."},
                {"id": "Y3A8", "question": "Which synchronization primitive is commonly used to control shared resource access?", "options": ["Semaphore", "Compiler", "Router", "Loop"], "answer": "Semaphore", "explanation": "Semaphores coordinate access to shared resources."},
                {"id": "Y3A9", "question": "Testing individual modules separately is called ____ testing.", "options": ["unit", "integration", "system", "acceptance"], "answer": "unit", "explanation": "Unit testing focuses on the smallest testable components."},
                {"id": "Y3A10", "question": "Which topology uses a central connecting device?", "options": ["Star", "Bus", "Ring", "Mesh"], "answer": "Star", "explanation": "A star topology connects all nodes to one central device."}
            ]
        },
        {
            "id": "section_b",
            "title": "Section B: True or False",
            "question_type": "true_false",
            "marks_per_question": 2,
            "questions": [
                {"id": "Y3B1", "question": "Every foreign key must contain only unique values.", "options": ["True", "False"], "answer": "False", "explanation": "Many rows can reference the same parent record."},
                {"id": "Y3B2", "question": "TCP guarantees ordered delivery of packets.", "options": ["True", "False"], "answer": "True", "explanation": "TCP provides reliable, ordered delivery."},
                {"id": "Y3B3", "question": "Virtual memory allows programs to use more memory than the physical RAM alone.", "options": ["True", "False"], "answer": "True", "explanation": "Virtual memory extends usable memory using disk-backed storage."},
                {"id": "Y3B4", "question": "Round robin scheduling is a non-preemptive scheduling algorithm.", "options": ["True", "False"], "answer": "False", "explanation": "Round robin is preemptive because it uses time slices."},
                {"id": "Y3B5", "question": "The SQL UPDATE command modifies existing records.", "options": ["True", "False"], "answer": "True", "explanation": "UPDATE changes values in rows that already exist."},
                {"id": "Y3B6", "question": "HTTP is a stateless protocol.", "options": ["True", "False"], "answer": "True", "explanation": "HTTP does not automatically remember earlier requests."},
                {"id": "Y3B7", "question": "In a star topology, each node directly connects to every other node.", "options": ["True", "False"], "answer": "False", "explanation": "Nodes connect to the center, not directly to every other node."},
                {"id": "Y3B8", "question": "Deadlock can happen when mutually exclusive resources are held and awaited.", "options": ["True", "False"], "answer": "True", "explanation": "Competing processes can block each other in this situation."},
                {"id": "Y3B9", "question": "Database transactions are expected to follow ACID properties.", "options": ["True", "False"], "answer": "True", "explanation": "ACID protects transaction correctness and reliability."},
                {"id": "Y3B10", "question": "Black-box testing depends on reading the internal source code implementation.", "options": ["True", "False"], "answer": "False", "explanation": "Black-box testing focuses on inputs and outputs."}
            ]
        },
        {
            "id": "section_c",
            "title": "Section C: Fill in the Blanks",
            "question_type": "fill_blank",
            "marks_per_question": 1,
            "questions": [
                {"id": "Y3C1", "question": "The SQL command used to add a new row is ____.", "answer": "insert", "explanation": "INSERT adds new rows to a table."},
                {"id": "Y3C2", "question": "The device that forwards packets between networks is a ____.", "answer": "router", "explanation": "Routers move packets between networks."},
                {"id": "Y3C3", "question": "A process waiting for CPU allocation is in the ____ state.", "answer": "ready", "explanation": "Ready processes are waiting to be scheduled."},
                {"id": "Y3C4", "question": "The command used to permanently save a transaction is ____.", "answer": "commit", "explanation": "COMMIT makes transaction changes permanent."},
                {"id": "Y3C5", "question": "The smallest independently testable software component is often a ____.", "answer": "unit", "explanation": "A unit is the smallest piece commonly tested in isolation."},
                {"id": "Y3C6", "question": "IP stands for Internet ____.", "answer": "protocol", "explanation": "IP is short for Internet Protocol."},
                {"id": "Y3C7", "question": "Function calls are commonly managed using the ____.", "answer": "stack", "explanation": "The call stack stores active function frames."},
                {"id": "Y3C8", "question": "A key in one table that refers to another table is called a ____ key.", "answer": "foreign", "explanation": "Foreign keys create relationships between tables."},
                {"id": "Y3C9", "question": "The loopback IP address commonly starts with ____.", "answer": "127", "explanation": "Loopback addresses use the 127.x.x.x range."},
                {"id": "Y3C10", "question": "In a star topology, the central connecting device is often a ____.", "answer": "switch", "explanation": "A switch commonly sits at the center of a star network."}
            ]
        }
    ]
}
YEAR_4_PAPER = {
    "paper_title": "Year 4 Emerging Technologies Assessment",
    "sections": [
        {
            "id": "section_a",
            "title": "Section A: MCQs",
            "question_type": "mcq",
            "marks_per_question": 2,
            "questions": [
                {"id": "Y4A1", "question": "Which type of learning uses labeled data?", "options": ["Supervised learning", "Unsupervised learning", "Reinforcement only", "Federated storage"], "answer": "Supervised learning", "explanation": "Supervised learning trains on input-output pairs."},
                {"id": "Y4A2", "question": "Which three ideas form the CIA triad in cybersecurity?", "options": ["Confidentiality, Integrity, Availability", "Control, Inspection, Access", "Cipher, Identity, Audit", "Compliance, Integration, Analysis"], "answer": "Confidentiality, Integrity, Availability", "explanation": "The CIA triad is a core security model."},
                {"id": "Y4A3", "question": "Which attack often tricks users into revealing passwords through fake messages?", "options": ["Phishing", "Compression", "Caching", "Sharding"], "answer": "Phishing", "explanation": "Phishing uses deceptive messages to steal sensitive information."},
                {"id": "Y4A4", "question": "Docker is primarily used to package applications into ____.", "options": ["containers", "threads", "sockets", "tables"], "answer": "containers", "explanation": "Docker bundles applications and dependencies into containers."},
                {"id": "Y4A5", "question": "Which cloud service model mainly provides virtual machines and infrastructure resources?", "options": ["IaaS", "SaaS", "PaaS", "DBaaS"], "answer": "IaaS", "explanation": "Infrastructure as a Service provides compute and networking resources."},
                {"id": "Y4A6", "question": "Overfitting happens when a model ____.", "options": ["memorizes training data too closely", "fails to read labels", "removes all noise", "stores no parameters"], "answer": "memorizes training data too closely", "explanation": "An overfit model struggles to generalize to new data."},
                {"id": "Y4A7", "question": "Which tool is commonly used for version control and branching?", "options": ["Git", "NumPy", "Postman", "SQLite"], "answer": "Git", "explanation": "Git tracks code history and supports branching workflows."},
                {"id": "Y4A8", "question": "What does two-factor authentication add to a login flow?", "options": ["A second verification step", "A faster CPU", "A local database", "A larger password"], "answer": "A second verification step", "explanation": "2FA requires another proof of identity beyond a password."},
                {"id": "Y4A9", "question": "REST APIs commonly use which data format for request and response bodies?", "options": ["JSON", "BMP", "EXE", "PDF"], "answer": "JSON", "explanation": "JSON is lightweight and widely used for APIs."},
                {"id": "Y4A10", "question": "Which platform is commonly used for orchestrating containers at scale?", "options": ["Kubernetes", "Photoshop", "Bluetooth", "Flask"], "answer": "Kubernetes", "explanation": "Kubernetes automates deployment and scaling of containers."}
            ]
        },
        {
            "id": "section_b",
            "title": "Section B: True or False",
            "question_type": "true_false",
            "marks_per_question": 2,
            "questions": [
                {"id": "Y4B1", "question": "Encryption turns readable plaintext into unreadable ciphertext.", "options": ["True", "False"], "answer": "True", "explanation": "Encryption protects data by converting it into ciphertext."},
                {"id": "Y4B2", "question": "Higher training accuracy always guarantees better real-world performance.", "options": ["True", "False"], "answer": "False", "explanation": "A model can overfit the training data and still generalize poorly."},
                {"id": "Y4B3", "question": "Kubernetes is used to manage containerized applications.", "options": ["True", "False"], "answer": "True", "explanation": "Kubernetes manages deployment and scaling of containers."},
                {"id": "Y4B4", "question": "A public cloud deployment is always cheaper for every workload.", "options": ["True", "False"], "answer": "False", "explanation": "Cost depends on workload and usage patterns."},
                {"id": "Y4B5", "question": "Hashing is intended to be directly reversible like decryption.", "options": ["True", "False"], "answer": "False", "explanation": "Hashing is designed as a one-way transformation."},
                {"id": "Y4B6", "question": "Cross-site scripting can inject malicious scripts into a browser context.", "options": ["True", "False"], "answer": "True", "explanation": "XSS attacks execute malicious scripts in a user's browser."},
                {"id": "Y4B7", "question": "A/B testing compares two variants to measure performance differences.", "options": ["True", "False"], "answer": "True", "explanation": "A/B testing compares two versions using real usage data."},
                {"id": "Y4B8", "question": "Maintaining backups can help recover from ransomware incidents.", "options": ["True", "False"], "answer": "True", "explanation": "Reliable backups support recovery when primary data is compromised."},
                {"id": "Y4B9", "question": "Precision and recall are classification metrics.", "options": ["True", "False"], "answer": "True", "explanation": "Precision and recall are standard classification evaluation metrics."},
                {"id": "Y4B10", "question": "A VPN can encrypt traffic between a user and a network gateway.", "options": ["True", "False"], "answer": "True", "explanation": "VPNs create an encrypted tunnel between endpoints."}
            ]
        },
        {
            "id": "section_c",
            "title": "Section C: Fill in the Blanks",
            "question_type": "fill_blank",
            "marks_per_question": 1,
            "questions": [
                {"id": "Y4C1", "question": "The practice of automating build, test, and deployment work is called ____.", "answer": "devops", "explanation": "DevOps combines development and operations practices."},
                {"id": "Y4C2", "question": "Learning from labeled examples is called ____ learning.", "answer": "supervised", "explanation": "Supervised learning uses labeled training data."},
                {"id": "Y4C3", "question": "Turning ciphertext back into readable text is called ____.", "answer": "decryption", "explanation": "Decryption restores encrypted data to plaintext."},
                {"id": "Y4C4", "question": "Software delivered directly over the internet is often offered as ____.", "answer": "saas", "explanation": "Software as a Service delivers ready-to-use applications online."},
                {"id": "Y4C5", "question": "A distributed version control system widely used by developers is ____.", "answer": "git", "explanation": "Git is the most widely used distributed version control system."},
                {"id": "Y4C6", "question": "A fake message designed to steal credentials is a ____ attack.", "answer": "phishing", "explanation": "Phishing attacks trick users into revealing sensitive data."},
                {"id": "Y4C7", "question": "The metric that measures correct positive predictions among all predicted positives is ____.", "answer": "precision", "explanation": "Precision measures the quality of positive predictions."},
                {"id": "Y4C8", "question": "A small independently deployable service is called a ____.", "answer": "microservice", "explanation": "Microservices split applications into smaller services."},
                {"id": "Y4C9", "question": "The technique used to update neural network weights is called ____.", "answer": "backpropagation", "explanation": "Backpropagation computes gradients for weight updates."},
                {"id": "Y4C10", "question": "A shared online repository like GitHub is commonly used for team ____.", "answer": "collaboration", "explanation": "Platforms like GitHub support team collaboration on code."}
            ]
        }
    ]
}


QUESTION_BANKS = {
    1: YEAR_1_PAPER,
    2: YEAR_2_PAPER,
    3: YEAR_3_PAPER,
    4: YEAR_4_PAPER,
}


def normalize_answer(value):
    return re.sub(r"\s+", " ", str(value or "").strip().lower())


def build_exam_from_paper(exam_paper, year_group, student_id):
    if not exam_paper:
        raise ValueError("Invalid exam paper")

    exam_paper = copy.deepcopy(exam_paper)
    rng = random.Random(f"{year_group}-{student_id}")

    for section in exam_paper["sections"]:
        rng.shuffle(section["questions"])

        for question in section["questions"]:
            question["type"] = section["question_type"]
            question["marks"] = section["marks_per_question"]

            if section["question_type"] == "mcq":
                option_rng = random.Random(f"{student_id}-{year_group}-{question['id']}")
                option_rng.shuffle(question["options"])

    return exam_paper


def build_exam_for_student(year_group, student_id):
    if year_group not in QUESTION_BANKS:
        raise ValueError("Invalid year group")
    return build_exam_from_paper(QUESTION_BANKS[year_group], year_group, student_id)

def grade_exam_submission_from_paper(exam_paper, year_group, student_id, answers):
    exam_paper = build_exam_from_paper(exam_paper, year_group, student_id)
    submitted_answers = answers or {}

    total_score = 0
    total_marks = 0
    section_results = []

    for section in exam_paper["sections"]:
        section_score = 0
        section_total = len(section["questions"]) * section["marks_per_question"]
        total_marks += section_total
        questions = []

        for index, question in enumerate(section["questions"], start=1):
            user_answer = str(submitted_answers.get(question["id"], "")).strip()
            is_correct = normalize_answer(user_answer) == normalize_answer(question["answer"])
            awarded_marks = question["marks"] if is_correct else 0
            section_score += awarded_marks

            questions.append({
                "id": question["id"],
                "number": index,
                "type": question["type"],
                "question": question["question"],
                "options": question.get("options", []),
                "correct_answer": question["answer"],
                "user_answer": user_answer or "Not Answered",
                "is_correct": is_correct,
                "explanation": question["explanation"],
                "marks_awarded": awarded_marks,
                "marks_possible": question["marks"],
            })

        total_score += section_score
        section_results.append({
            "id": section["id"],
            "title": section["title"],
            "question_type": section["question_type"],
            "score": section_score,
            "total": section_total,
            "questions": questions,
        })

    return {
        "paper_title": exam_paper["paper_title"],
        "year_group": year_group,
        "total_score": total_score,
        "total_marks": total_marks,
        "section_results": section_results,
    }


def grade_exam_submission(year_group, student_id, answers):
    if year_group not in QUESTION_BANKS:
        raise ValueError("Invalid year group")
    return grade_exam_submission_from_paper(QUESTION_BANKS[year_group], year_group, student_id, answers)
