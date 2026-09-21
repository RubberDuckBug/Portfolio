# Portfolio
Website that contains my portfolio

### For loading into a virtual environment + dependencies
venv\Scripts\activate  
pip install -r requirements.txt

### Dev run
python app.py

### AWS Services used:
- IAM (Identity and Access Management): Account to work on website
- SES (Simple Email Service): Sends emails
- RDS (Relational Database Service): An always-on database running on a cloud server
- Elastic Beanstalk: Manages everything that the website requires (servers, deployment)
- EC2 (Elastic Compute Cloud): The physical machine that runs the website (only Beanstalk needs access to this)
- VPC: Firewall/Security
- CodePipeline: Auto-deploys git pushes to the website


### Creator - RubberDuckBug
