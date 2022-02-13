# JenkinsInAction

## CI-CD

### Sample pipeline flow
<img src="https://i.imgur.com/dXOG2yn.png" />

### CI/CD (Delivery vs Deployment)
<img src="https://i.imgur.com/oV260ke.png" />

## Install Jenkins
* Update Repo List
    
    ```apt-get update```
* Installing JDK
	
    ```apt-get install default-jdk```
* Adding the key 

    ```wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -```
* Adding the repo path
  	
    ```echo "deb https://pkg.jenkins.io/debian-stable binary/" > /etc/apt/sources.list.d/jenkins.list```
* Update repo list
	
     ```apt-get update```
* Install jenkins
	    
    ```apt-get install jenkins```
* Check the jenkins service status
	    
    ```service jenkins status```

## Allow traffic on port 8080 on the AWS VM
* Go to Instances in the AWS
* Select your Instance
* In the bottom pane, click on `Security`
* Click on the name of `Security Group` listed there
* Now you will get landed to the Security Group page
* There click on `Edit Inbound Rules`
* Click on `Add Rule`
* In the `Port Range` prompt, specify `8080` and choose the source as `Anywhere IPv4`
* Click on Save Rules

* Now you can access the web page in the browser using Public Ip of the VM

## Initial Setup Jenkins 
* Open your jenkins in the browser using vm_ip:8080
* Now you need to provide the initial admin password in order to move ahead
* Just get the password by running the below command on your jenkins server
	
    ```cat /var/lib/jenkins/secrets/initialAdminPassword```
* Now go to browse, provide the password you got in previous command
* Click on Select Plugins to install
* Now just unselect all the selected one, by clicking on None button
* Click Install
* Provide your credentials
* Click on save and continue
* Click on save and finish 
* Click on start using Jenkins



## Creating first Job in Jenkins
- Go to your Jenkins Dashboard
- Click on the `New Item` button located on the top left corner
- Then define a name for your Job
- Select Freestyle project over there
- Click on `OK` button
- Scroll Down and under the `Build` section, click on `Add Build`, then `Execute Shell`
- Now put the below set of commands in that textbox

    ```
    touch file1
    ls -l
    ```
- Click on Save button
- That's it your job got created, just click on `Build Now` button located in the left bar to execute it

## Periodic Job in Jenkins
- Go to your Jenkins Dashboard
- Click on the `New Item` button located on the top left corner
- Then define a name for your Job
- Select Freestyle project over there
- Click on `OK` button
- Under `Build Triggers`, just select the option stating `Build Periodically` and define `*/2 * * * *` expression in that
- Scroll Down and under the `Build` section, click on `Add Build`, then `Execute Shell`
- Now put the below set of commands in that textbox

    ```
    date
    ```
- Click on Save button


## Running Jenkins as a Java Process using war file
- Switch to root user

    ```sudo su```
- Update the repo list

    ```apt-get update```
- Install java

    ```apt-get install default-jdk```
- Download Jenkins war file

    ``` wget https://get.jenkins.io/war-stable/2.303.3/jenkins.war```
- Run Jenkins
    
    ```java -jar jenkins.war```
- Now your Jenkins started, just browse it using vm_ip:8080
- There it will prompt you for inital admin password, just take from the output of your last command and then proceed
* Click on Select Plugins to install
* Now just unselect all the selected one, by clicking on None button
* Click Install
* Provide your credentials
* Click on save and continue
* Click on save and finish 
* Click on start using Jenkins

- Start Jenkins in background

    ```nohup java -jar jenkins.war &```


## Parameterized Job in Jenkins
- Go to your Jenkins Dashboard
- Click on the `New Item` button located on the top left corner
- Then define a name for your Job
- Select Freestyle project over there
- Click on `OK` button
- In the general section, just check the box stating `This project is parameterized`.
- Click on `Add Parameter`, -> `String Parameter`
- Define a name for your parameter
- If you wish you can define some default value as well for that
- Scroll Down and under the `Build` section, click on `Add Build`, then `Execute Shell`
- Now put the below set of commands in that textbox

    ```
    echo $your_variable_name
    ```
- Click on Save button
- That's it your job got created, just click on `Build With Parameters` button located in the left bar to execute it
- This time, it will prompt you for inputs, kindly provide the value and witness magic

## Integrating Gitlab Repo with Jenkins
- Installing Plugin
    - Go to Jenkins Dashboard
    - Click on `Manage Jenkins`
    - Click on `Manage Plugins`
    - Click on `Available`
    - Search for `Gitlab` in that
    - Select the checkbox stating `Gitlab` and click on `Install without Restart`

- Creating Job with SCM defined
    - Go to your Jenkins Dashboard
    - Click on the `New Item` button located on the top left corner
    - Then define a name for your Job
    - Select Freestyle project over there
    - Click on `OK` button
    - Under SCM, select `Git` and the put the repository address as `https://gitlab.com/konnectchetan/java-demo-app`
    - Scroll Down and under the `Build` section, click on `Add Build`, then `Execute Shell`
    - Now put the below set of commands in that textbox

        ```
        ls -l
        ```
    - Click on Save button
    - That's it your job got created, just click on `Build Now` button located in the left bar to execute it, and the in the console output you can see the repository code


## Using Jenkins Environment Variables in the Job
- Creating Job with SCM defined and variables used
    - Go to your Jenkins Dashboard
    - Click on the `New Item` button located on the top left corner
    - Then define a name for your Job
    - Select Freestyle project over there
    - Click on `OK` button
    - Under SCM, select `Git` and the put the repository address as `https://gitlab.com/konnectchetan/java-demo-app`
    - Scroll Down and under the `Build` section, click on `Add Build`, then `Execute Shell`
    - Now put the below set of commands in that textbox

        ```
        echo "The build number is --> "$BUILD_NUMBER
        echo "Commit iD is  --> "$GIT_COMMIT
        echo "Job URL is --> "$RUN_DISPLAY_URL
        ```
    - Click on Save button
    - That's it your job got created, just click on `Build Now` button located in the left bar to execute it, and the in the console output you can see the repository code


## Forking the Repo in GITLAB account for further labs
- Let's fork the repo in your account
    - Open the link `https://gitlab.com/konnectchetan/java-demo-app`
    - Click on `Fork` button
    - In select namespace drop down, select your respective user
    - Change visibility to `public`
    - Click on `Fork` Project
- Making changes to the Repo via Gitlab Interface
    - Go the Repo Page
    - Click on any `README.md`
    - Click on the `button` located along with `Edit` or `Edit in Web IDE` 
    - Click on `Edit` in the dropdown which appears
    - Now click on the `Edit` button, it will open the file for editing purposes in the browser for you
    - Make changes to the file
    - Click on `Commit Changes` button


## Poll SCM - Lab

- Poll SCM will make your jenkins check with Remote Repo for new updates on the basis frequency you have defined. 
- It will execute the job only in the case, when it found some changes in the repository. It is figuring out the changes by comparing the commit id in the last build and last commit id in github.
- We need to define a schedule in the form cron expression. 
- Let's say, you defined the expression as (*/2 * * * *), which equivalent to every 2nd minute. Now for this, jenkins will check for updates in to the repository every 2nd minute, if it found any new change, then it will trigger the job, otherwise not.

<img src="https://i.imgur.com/YM7Y1EB.png" />

- Creating Job
    - Go to your Jenkins Dashboard
    - Click on the `New Item` button located on the top left corner
    - Then define a name for your Job
    - Select Freestyle project over there
    - Click on `OK` button
    - Under SCM, select `Git` and the put your `Forked`repository address 
    - Under `Build Triggers` option, just select `Poll SCM` and then define a schedule, let's every minute `* * * * *`
    - Scroll Down and under the `Build` section, click on `Add Build`, then `Execute Shell`
    - Now put the below set of commands in that textbox

        ```
        ls -l
        ```
    - Click on Save button
    - That's it your job got created, 
    - Just push some code on to your repository, and as per the polling mechanism, it will automatically execute

## Webhook Based Triggers
<img src="https://i.imgur.com/Qrm2sWJ.png" />

### Gitlab Webhooks based trigger
- Creating Job
    - Go to your Jenkins Dashboard
    - Click on the `New Item` button located on the top left corner
    - Then define a name for your Job
    - Select Freestyle project over there
    - Click on `OK` button
    - Under SCM, select `Git` and the put your repository address 
    - Under `Build Triggers` option, just select `Build when a change is pushed to GitLab`, Along with this option you will see a url over there, that is your hook URL, just copy this
    - Scroll Down and under the `Build` section, click on `Add Build`, then `Execute Shell`
    - Now put the below set of commands in that textbox

        ```
        ls -l
        ```
    - Click on Save button
    - That's it your job got created, 
- Let's create a API token for current user only
    - Go to Jenkins Dashboard
    - In the left pane, click on `Manage Jenkins` -> `Manage Users`
    - Click on your specific user 
    - Click on `Configure` in the left pane
    - Click on `Add New API Token`, put some name in the text box and click on `Generate` button, now just copy the token value and keep it safe
    - Click on Save button, to save user changes
- Adding the Webhook Address in the repository
    - Go to your Gitlab Repository page
    - Click on  `Settings` over there
    - In the left pane, click on `Webhooks`
    - Now your hook address would be like `http://username:token@jenkins_url/project/JobName`, so what you need to do, just add `username:token@` before url jenkins IP in the URL you copied
    - Click on `Add Webhook`
- Just push some code on to your repository, and you will see your Job getting triggered automatically

### Github Webhooks based trigger

- Adding the Webhook Address in the repository
    - Go to your Github Repository page
    - Click on `Settings` over there
    - In the left pane, click on `Webhooks`
    - Click on `Add Webhook`
    - Add the webhook address over there `jenkins_url/github-webhook/`
    - Click on `Add Webhook`
- Creating Job
    - Go to your Jenkins Dashboard
    - Click on the `New Item` button located on the top left corner
    - Then define a name for your Job
    - Select Freestyle project over there
    - Click on `OK` button
    - Under SCM, select `Git` and the put your repository address 
    - Under `Build Triggers` option, just select `GitHub hook trigger for GITScm polling`
    - Scroll Down and under the `Build` section, click on `Add Build`, then `Execute Shell`
    - Now put the below set of commands in that textbox

        ```
        ls -l
        ```
    - Click on Save button
    - That's it your job got created, 
    - Just push some code on to your repository, and you will see your Job getting triggered automatically

### Bitbucket Webhooks based trigger
- Installing Plugin
    - Go to Jenkins Dashboard
    - Click on `Manage Jenkins`
    - Click on `Manage Plugins`
    - Click on `Available`
    - Search for `Bitbucket` in that
    - Select the checkbox stating `Bitbucket` and click on `Install without Restart`
- Adding the Webhook Address in the repository
    - Go to your Bitbucket Repository page
    - Click on `Repository Settings` over there
    - In the left pane, click on `Webhooks`
    - Click on `Add Webhook`
    - Add the webhook address over there `jenkins_url/bitbucket-hook/`
    - Click on `Add Webhook`
- Creating Job
    - Go to your Jenkins Dashboard
    - Click on the `New Item` button located on the top left corner
    - Then define a name for your Job
    - Select Freestyle project over there
    - Click on `OK` button
    - Under SCM, select `Git` and the put your repository address 
    - Under `Build Triggers` option, just select `Build when a change is pushed to BitBucket`
    - Scroll Down and under the `Build` section, click on `Add Build`, then `Execute Shell`
    - Now put the below set of commands in that textbox

        ```
        ls -l
        ```
    - Click on Save button
    - That's it your job got created, 
    - Just push some code on to your repository, and you will see your Job getting triggered automatically

## Integrating Private Repositories using HTTPS based URLs
- Make sure you have private repository in your account if not, kindly fork below stated repo in your account and keep it as private 
    - Open the link `https://gitlab.com/konnectchetan/node-demo`
    - Click on `Fork` button
    - In select namespace drop down, select your respective user
    - Change visibility to `private`
    - Click on `Fork` Project
- Let's create credentials
    - Go to Jenkins Dashboard
    - Click on `Manage Jenkins` -> `Manage Credentials` ->  `Jenkins` -> `Global Credentials`
    - In the left pane, click on `Add Credentials`
    - Select kind as `Username and password`
    - Put the your Gitlab user name in the `username` prompt and your password in the `password` prompt
    - Define some name in `id` text box
    - Click on Ok
- Create the Job
    - Go to your Jenkins Dashboard
    - Click on the `New Item` button located on the top left corner
    - Then define a name for your Job
    - Select Freestyle project over there
    - Click on `OK` button
    - Under SCM, select `Git` and the put the Forked Private Repository URL
    - Under credentials, select the one which you created right now in the above step
    - Under Build, select `Execute Shell` and put the below in the text box

        ```ls -l```
    - Save the job
    - Execute it and you will see this one working

## Maven Execution using Jenkins
- Configuring Maven Installer
    - Go to Jenkins Dashboard
    - Click on `Manage Jenkins` -> `Global Tool Configuration`
    - Scroll Down, look for Maven, and click on `Add Maven`
    - Define a name for your installer
    - Click on Save button
- Let's create the JOB
    - Go to your Jenkins Dashboard
    - Click on the `New Item` button located on the top left corner
    - Then define a name for your Job
    - Select Freestyle project over there
    - Click on `OK` button
    - Under SCM, select `Git` and the put your repository address as `https://gitlab.com/konnectchetan/java-demo-app` 
    - Scroll Down and under the `Build` section, click on `Add Build`, then `Invoke Top Level Maven Targets`
    - Select the maven installer which you configured in the previous step
    - Put goal as `package`
    - Click on Save button
    - That's it your job got created
    - You can execute it, by clicking on `Build Now`, you will see the project getting processed and war getting generated for you.




## SonarCloud Setup
- Let's generate the token 
    - Go to `https://gitlab.com/-/profile`
    - In the left pane, click on 'Access Tokens'
    - Then define some name for token, set expiry if you wish to
    - Then under permissions, just check the box stating `api`
    - Click on `Create personal access token`
    - Now copy the token which you will get
- Let's setup sonar cloud
    - Go to https://sonarcloud.io/
    - Login with Gitlab
    - Click on Authorize to login with Gitlab in SonarCloud
    - Click on `Import any Organisation`
    - Then it will prompt your for Import Project, just select the option stating `Import my Personal Gitlab Group`
    - Now it will prompt for Token, put the copied token in the prompt
    - Then click on `Continue`
    - Select `Free Plan`
    - Click on `Create Organisation`
    - Now select the Repository `Java Demo App`
    - Click on `Setup`
- Let's install the plugin for Sonar on jenkins
    - Installing Plugin
        - Go to Jenkins Dashboard
        - Click on `Manage Jenkins`
        - Click on `Manage Plugins`
        - Click on `Available`
        - Search for `SonarQube` in that
        - Select the checkbox stating `SonarQube Scanner` and click on `Install without Restart`
- Configuring Sonar Scanner Installer
    - Go to Jenkins Dashboard
    - Click on `Manage Jenkins` -> `Global Tool Configuration`
    - Scroll Down, look for SonarQube Scanner, and click on `Add SonarQube Scanner`
    - Define a name for your installer
    - Click on Save button
- Create token for Sonar Cloud access by Jenkins
    - Go to `https://sonarcloud.io/account/security/`
    - Just put some name for token over there and click on Generate
    - Copy the token which got generated
- Let's create credentials in Jenkins to store the Token
    - Go to Jenkins Dashboard
    - Click on `Manage Jenkins` -> `Manage Credentials` ->  `Jenkins` -> `Global Credentials`
    - In the left pane, click on `Add Credentials`
    - Select kind as `Secret Text`
    - Put the copied token in the `Secret` text box
    - Define some name in `id` text box
    - Click on Ok
- Add the Sonar Qube address
    - Go to Jenkins Dashboard
    - Click on `Manage Jenkins` -> `Configure System`
    - Scroll Down, look for SonarQube servers, and click on `Add SonarQube`
    - Give any name
    - Put Sever Url as `https://sonarcloud.io/`
    - Select the token which you created in previous step for the dropdown asking `Server authentication token`
    - Click on Save button
- Get the values from `Sonar` Project page
    - Go to SonarQube Cloud Project page. 
    - There on the left pane, click on `information`, 
    - Then copy the two values stating `organization key` and `project key`
    
- Creating Job
    - Go to your Jenkins Dashboard
    - Click on the `New Item` button located on the top left corner
    - Then define a name for your Job
    - Select Freestyle project over there
    - Click on `OK` button
    - Under SCM, select `Git` and the put your Forked Repository address 
    - Under Build, click on `Add Build` once again, and select `Execute SonarQube Scanner`
    - Now we need to provide, Analysis Properties for Sonar, just add the below stuff by replacing your values which you got in previous step
    
        ```
        sonar.organization=
        sonar.projectKey=
        sonar.sources=. 
        ```
    - Click on Save button
    - That's it your job got created, 
    - You can build the job, see the report in SonarQube.

## Ansible Integration with Jenkins
- Install Ansible on the Jenkins Server
    - Switch to root user (if not already)
        
        ```sudo su```
    - Update Repo List

        ```apt-get update```
    - Add repo path
        
        ```add-apt-repository ppa:ansible/ansible```
    - Install Ansible

        ```apt-get install ansible```
- Installing Plugin
    - Go to Jenkins Dashboard
    - Click on `Manage Jenkins`
    - Click on `Manage Plugins`
    - Click on `Available`
    - Search for `Ansible` in that
    - Select the checkbox stating `Ansible` and click on `Install without Restart`
- Create the Job
    - Go to your Jenkins Dashboard
    - Click on the `New Item` button located on the top left corner
    - Then define a name for your Job
    - Select Freestyle project over there
    - Click on `OK` button
    - Under SCM, select `Git` and the put "https://gitlab.com/synechron-jenkins-workshop-nov-21/ansible-demo-jenkins/"
    - Change the branch name to `main`
    - Scroll Down and under the `Build` section, click on `Add Build`, then `Invoke Ansible Playbook`
    - Put playbook path as `demo.yaml`
    - Select Inventory as `File or Host list` and the put `inventory` in the text box
    - Click on Save button
    - That's it your job got created, 
    - You can build the job, and see the ansible making its changes.

## Integrating Docker with Jenkins
- Install Docker and Make docker commands executable via jenkins user
    - Update Repo List
        
        ```apt-get update```
    - Install docker
    
        ```apt-get install docker.io```
    - Give permission to jenkins user

        ```usermod -aG docker jenkins```
    - Restart jenkins

        ```service jenkins restart```
- Create the Job
    - Go to your Jenkins Dashboard
    - Click on the `New Item` button located on the top left corner
    - Then define a name for your Job
    - Select Freestyle project over there
    - Click on `OK` button
    - Under SCM, select `Git` and the put "https://gitlab.com/synechron-jenkins-workshop-nov-21/java-demo-app/"
    - Change the branch name to `master`
    - Scroll Down and under the `Build` section, click on `Add Build`, then `Invoke Top Level maven Targets`
    - Select the Maven Installer and put the goal as `package`
    - Under the `Build` section, click on `Add Build`, then `Execute Shell`
    - Put the below command `docker build -t myapp -f docker .`
    - Note: You can also create a container like docker container run -itd -p 83:8080 myapp
    - Click on Save button
    - That's it your job got created, 
    - You can build the job, and see the ansible making its changes.

## Integrating Private Repositories using HTTPS based URLs
- Make sure you have private repository in your account if not, kindly fork below stated repo in your account and keep it as private https://gitlab.com/konnectchetan/node-demo
- Let's create credentials
    - Go to Jenkins Dashboard
    - Click on `Manage Jenkins` -> `Manage Credentials` ->  `Jenkins` -> `Global Credentials`
    - In the left pane, click on `Add Credentials`
    - Select kind as `Username and password`
    - Put the your Gitlab user name in the `username` prompt and your password in the `password` prompt
    - Define some name in `id` text box
    - Click on Ok
- Create the Job
    - Go to your Jenkins Dashboard
    - Click on the `New Item` button located on the top left corner
    - Then define a name for your Job
    - Select Freestyle project over there
    - Click on `OK` button
    - Under SCM, select `Git` and the put the Forked Private Repository URL
    - Under credentials, select the one which you created right now in the above step
    - Under Build, select `Execute Shell` and put the below in the text box

        ```ls -l```
    - Save the job
    - Execute it and you will see this one working

## Integrating Private Repositories using SSH based URLs
- Let's generate SSH Keys
    - Go to your VM
    - Run the below command

        ```ssh-keygen```
    - This command will prompt you for certain inputs 3-4 times, just press `enter` to keep the default
    - After this you will have your Public and private Key generated.
    - In the output, you will see certain lines like this

        ```
        Your identification has been saved in some_path
        Your public key has been saved in some_path
        ```
    - Here you can see, the path of your public key and private key, just note them
- Let's add the public key in the repository
    - First of call copy the content of public key which you generated in the previous step

        ```cat copied_path_of_public_key```
    - Copy the output which you got
    - Now, go to the repository page
    - In the left pane, click on `Settings` -> `Repository`
    - Click on `Expand` corresponding to `Deploy keys`
    - Here, put some title, and paste the copied key in the Key textbox over there
    - Click on Add Key
- Let's create credentials in jenkins for private key
    - First of call copy the content of private key which you generated in the previous step

        ```cat copied_path_of_private_key```
    - Copy the output which you got
    - Go to Jenkins Dashboard
    - Click on `Manage Jenkins` -> `Manage Credentials` ->  `Jenkins` -> `Global Credentials`
    - In the left pane, click on `Add Credentials`
    - Select kind as `SSH username with private key`
    - Define some name in `id` text box
    - Put the username as `jenkins` if your jenkins is running in form of service, otherwise put `root` in the username section, if it is running as java process
    - Click on Private Key `Enter Directly`
    - Click on Add button, and paste the copied private key
    - Click on Ok
- Create the Job
    - Go to your Jenkins Dashboard
    - Click on the `New Item` button located on the top left corner
    - Then define a name for your Job
    - Select Freestyle project over there
    - Click on `OK` button
    - Under SCM, select `Git` and the put the SSH based url of your repository, which you can get by clicking on the `Clone` button on the Repo page.
    - Under credentials, select the one which you created right now in the above step
    - Under Build, select `Execute Shell` and put the below in the text box

        ```ls -l```
    - Save the job
    - Execute it and you will see this one working
    
## Setup Jenkins Agent
- Configuring Other machine
    - Log in to other VM
    - Switch to root user
    
        ```sudo su```
    - Change Hostname

        ```hostnamectl set-hostname agent```
        To reflect these changes, just do 
    
        ```
        exit
        sudo su
        ```
    - Now your machine shell will `root@agent`
    - Install Java
        - update repo list

            ```apt-get update```
        - Install java

            ```apt-get install default-jdk```
    - Let's create a directory on agent machine which will act as `workspace` for Jenkins

        ```mkdir /jenkins_data```
- Configure the port for Agent Communication
    - Go to jenkins dashboard
    - Click on `Manage Jenkins` -> `Configure Global Security`
    - Under agents, select `Fixed` and put the port number as `8081`
    - Save this
- You need to allow the traffic on port number specified over here i.e. `8081` on the Jenkins VM
- Let's add node in Jenkins Dashboard
    - Go to jenkins dashboard
    - Click on `Manage Jenkins` -> `Manage Nodes and Clouds`
    - In the left pane, click on `New Node`
    - Define some name for node, and select agent type as `Permanent Agent` and click `oK`
    - Define the Number of executer now
    - Put the remote directory as `/jenkins_data`
    - Put some label value, let's say `n1`
    - Under usage, select `Only build jobs with label expressions matching this node`
    - Put `Custom WorkDir Path` as `/jenkins_data`
    - Click on Save
    - You can see the node got added but the status is inactive, let's activate it
    - Click on node name
    - Now, you may see `agent.jar` listed over there, just do right click on that and copy the link location
    - Now just go to the agent machine and download this jar file with the below command

        ```wget copied_address```
    - To start the agent, just go the dashboard once again, from where you copied the address, now copy the command starting with `java -jar` and execute it on the agent machine
    - After execution, just refresh the web page, you will see it saying `Agent is connected`

## Running Jenkins Job on Agent
- Create the Job
    - Go to your Jenkins Dashboard
    - Click on the `New Item` button located on the top left corner
    - Then define a name for your Job
    - Select Freestyle project over there
    - Click on `OK` button
    - Under General, just check the box stating `Restrict where this project can be run`
    - Put the label which you defined while adding the node in the corresponding textbox, like we added `n1`
    - Under SCM, select `Git` and the put this repo url https://gitlab.com/synechron-jenkins-workshop-nov-21/java-demo-app
    - Under Build, select `Execute Shell` and put the below in the text box

        ```ls -l```
    - Save the job
    - Execute it and you will see this one running on `Node1`
## Role Based Access in Jenkins
- Create some users
    - Go to Jenkins Dashboard
    - Click on `Manage Jenkins` -> `Manage Users`
    - In the left pane, click on `Create User`
    - Then put the username, password, name and some email over there and click on `Create User`
- Repeat the above step for creating new users with name like `padev,paqa,pbdev,pbqa`
- Create 4 different jobs in Jenkins with the names like `ProjectA-Dev,ProjectA-QA,ProjectB-Dev,ProjectB-QA`
- Installing Plugin
    - Go to Jenkins Dashboard
    - Click on `Manage Jenkins`
    - Click on `Manage Plugins`
    - Click on `Available`
    - Search for `Role` in that
    - Select the checkbox stating `Role-based Authorization Strategy` and click on `Install without Restart`
- Changing Jenkins Security
    - Go to Jenkins Dashboard
    - Click on `Manage Jenkins` -> `Configure Global Security`
    - Under `Authorization` - Select ` Role-Based Strategy`
    - Click on Save button
- Creating Roles and Providing the access
    - Go to Jenkins Dashboard
    - Click on `Manage Jenkins` -> `Manage and Assign Roles`
    - Click on `Manage Roles`
    - Let's add the Global Role
        - Under Global Roles, put `team` under `Role to add` text box
        - Click on Add button
        - Corresponding to `team` role, check the box stating `Read` under `Overall` section
        - Scroll Down, click on Apply button
    - Let's add the Item Roles now
        - Under Items Roles, 
            - put `pad` under `Role to add` text box
            - put pattern as `ProjectA-Dev`
            - Click on Add button
            - put `paq` under `Role to add` text box
            - put pattern as `ProjectA-QA`
            - Click on Add button
        - Corresponding to `pad` and `paq` roles, check the box stating `Build,Discover,Read,Workspace` under `Job` section
        - Scroll Down, click on Save button
    - Let's assign these roles to the users which we created
        - Click on `Manage Jenkins` -> `Manage and Assign Roles`
        - Click on `Assign Roles`
        - Under Global Roles
            - put `padev` under `User/Group to add` text box
            - Click on Add Button
            - put `paqa` under `User/Group to add` text box
            - Click on Add Button
            - Corresponding to `padev` and `paqa` users, check the box corresponding to `team` role
            - Scroll Down, click on Apply button
        - Under Item Roles
            - put `padev` under `User/Group to add` text box
            - Click on Add Button
            - put `paqa` under `User/Group to add` text box
            - Click on Add Button
            - Corresponding to `padev`, check the box corresponding to `pad` role
            - Corresponding to `paqa`, check the box corresponding to `paq` role
            - Click on Save button
- Now we are done with all the settings, in a private you can open jenkins and try to login with your `padev` and `paqa` user respectively, you will see the granular access for them

## Using Patterns in Role Assignments
- Click on `Manage Jenkins` -> `Manage and Assign Roles`
- Click on `Manage Roles`
- Let's add the Item Roles now
    - Under Items Roles, 
        - put `dev` under `Role to add` text box
        - put pattern as `*.Dev`
        - Click on Add button
        - put `qa` under `Role to add` text box
        - put pattern as `*.QA`
        - Click on Add button
    - Corresponding to `dev` and `qa` roles, check the box stating `Build,Discover,Read,Workspace` under `Job` section
        - Scroll Down, click on Save button
- Let's assign these roles to the users which we created
    - Click on `Manage Jenkins` -> `Manage and Assign Roles`
    - Click on `Assign Roles`
    - Under Global Roles
        - put `pbdev` under `User/Group to add` text box
        - Click on Add Button
        - put `pbqa` under `User/Group to add` text box
        - Click on Add Button
        - Corresponding to `pbdev` and `pbqa` users, check the box corresponding to `team` role
        - Scroll Down, click on Apply button
    - Under Item Roles
        - put `pbdev` under `User/Group to add` text box
        - Click on Add Button
        - put `pbqa` under `User/Group to add` text box
        - Click on Add Button
        - Corresponding to `padev`, check the box corresponding to `dev` role
        - Corresponding to `paqa`, check the box corresponding to `qa` role
        - Click on Save button
- Now we are done with all the settings, in a private you can open jenkins and try to login with your `pbdev` and `pbqa` user respectively, you will see the granular access for them

## Pipelines
- Installing Plugin
    - Go to Jenkins Dashboard
    - Click on `Manage Jenkins`
    - Click on `Manage Plugins`
    - Click on `Available`
    - Search for `Pipeline` in that
    - Select the checkbox stating `Pipeline` and click on `Install without Restart`
- Creating Job
    - Go to Jenkins Dashboard
    - Click on `New Item`
    - Provide a name for your Job
    - Select it as `Pipeline`
    - Click on `OK`
    - Now scroll down, under pipeline textbox, just put the below code

    ```
    pipeline {
        agent any

        stages {
            stage('Stage1') {
                steps {
                    echo 'Step1'
                }
            }
            stage('Stage2'){
                steps{
                    echo 'Step2'
                }
            }
            stage('Stage3'){
                steps{
                    echo 'Step3'
                }
            }
            stage('Stage4'){
                steps{
                    echo 'Step4'
                }
            }
        }
    }
    ```
    - Click on Save
    - Click on `Build Now` to see this sample pipeline running.

## Pipeline Demo
- Creating Job
    - Go to Jenkins Dashboard
    - Click on `New Item`
    - Provide a name for your Job
    - Select it as `Pipeline`
    - Click on `OK`
    - Scroll Down, Under Pipeline Definition, just select `Pipeline Script from SCM`
    - Under SCM, select `Git`
    - Put the this repo address in Git `https://gitlab.com/synechron-jenkins-workshop-nov-21/java-demo-app`
    - Click on Save button
    - Click on Build to see this performing all these steps in a sequence
