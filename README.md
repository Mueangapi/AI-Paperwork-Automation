# Proof of Concept, eliminate unnecessary tasks.🪄

Welcome to my repo, if you're finding something to make an impact. I would recommend you to read this book.

![image](https://github.com/Mueangapi/I-m-gonna-disrupt-my-job-the-series-inspired-by-WEF-Future-of-jobs-doc./assets/104725034/27e7906e-c430-4c00-b084-bd1fa7c47700)

https://www.weforum.org/publications/the-future-of-jobs-report-2023/

They mentioned about what jobs and skills are in demand for the next 5 years, and what jobs are gonna be less needed!

It's interesting but I didn't have much time to read it. So.. let's find some solutions!

## 1st Chapter, I need an assistant.
and here is what i found https://platform.openai.com/docs/assistants/how-it-works
![image](https://github.com/Mueangapi/I-m-gonna-disrupt-my-job-the-series-inspired-by-WEF-Future-of-jobs-doc./assets/104725034/32b13a94-19b6-435d-9b45-1ba4c530d047)
![image](https://github.com/Mueangapi/I-m-gonna-disrupt-my-job-the-series-inspired-by-WEF-Future-of-jobs-doc./assets/104725034/c21a7413-8378-41ba-aadf-5f8a91095790)

So I try implementing it using Streamlit🍁(Clone my repo and run app.py)
```
$ cd app
$ streamlit run app.py
```
![image](https://github.com/Mueangapi/I-m-gonna-disrupt-my-job-the-series-inspired-by-WEF-Future-of-jobs-doc./assets/104725034/cf238f34-ad9a-487a-b5d5-0e4b1b9d2a05)

After took a journey I found so many possibilities, felt like having unlocked the ability to learn new thing quickly📖. As long as the assistant could simplify.

I found something really cauth my eye👀 as a current worker at a bank, It's the top lowest jobs here.
![image](https://github.com/Mueangapi/I-m-gonna-disrupt-my-job-the-series-inspired-by-WEF-Future-of-jobs-doc./assets/104725034/1967db26-9fa9-4ff3-b1ee-e58f9c7a04ac)

As an economics graduated like me, it's well known that the whole economy is run by credit. and I think I could find the gap in this opportunity.📊

## 2nd Chapter, Gathering infos and requirments.
 Firstly I think it necessary to understand what is credit officers. and which role are also involved.

 ![image](https://github.com/Mueangapi/AI-Automation/assets/104725034/102fd307-e44f-4f1c-bea8-6936279febb2)

 After conclude some informations, It seems like when a customer(I'm mentioning corporate) need money, it could be long or short term debt. The first person to meet our customer is The Relationship Manager(RM) who is gathering customer data, ask them for involved docs, and help initiating loans proposal.

 ![image](https://github.com/Mueangapi/AI-Automation/assets/104725034/656ab816-30e4-43d2-82c4-70687e83a892)

 Secondly they work with credit analyst, by passing them a loan proposal. which include objective of the loans, loans amount, balance sheet, etc. Now it's time for credit analyst who is spend most of the time analyze if they should approve a loans or not. Finally if the loans are approved they told operation team to help facility loans into customer's bank account.

 In summary I think RM spend most of the time with customers, The solution they needs might be monitoring <ins>dashboard</ins> or else helping they do the best at CRM (It could be a beer, wine or souvenirs😂). For the analyst they spend time with those document and analyze it then create a <ins>Credit Approval Document</ins>. They solution they need might be <ins>web application or some process automation</ins>.

 Alright Let's see what we can do Next!

 ## 3rd Chapter, Credit Approval Auto Generation Architecture.
 
Lets' see what component of Credit Approval document looks like. It's prohibit to provide the real one so..

![image](https://github.com/Mueangapi/AI-Automation/assets/104725034/7cf9c3e5-6257-4d66-b9d4-c77fc18d2dd1)

The document simply contains 
1. Text (headers)
2. Text (analysis of explanation)
3. Table
and then we're just put data from other sources into it. 

Now we need some framework or module to help doing it. I choose "python-docx" to help create word document, but we could only finish 1 and 3 part. The 2 part needs a brain to generate explanation of input we're gonna give( for example financial data, budget, and balance sheet). 
![image](https://github.com/Mueangapi/AI-Automation/assets/104725034/6884a6eb-4b85-43ea-91e7-d6124524f006)

Now let's design an architecture.
![image](https://github.com/Mueangapi/AI-Automation/assets/104725034/0027b0c2-996c-4436-bfdf-8ddcfcd4267f)

There are 2 main components that we need to know.
1. python-docx responsible for create word docx(Arrange text and table)
2. Lange Language Model (llm) responsible for generate human-like description of table or data.

## 4rd Chapter Start Coding.

 
