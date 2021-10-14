## HOW TO CONTRIBUTE TO THIS REPOSITORY.

**What is in this document?**
* [How to make non-code contribution](#making-non-code-contributions)
* [Making code contributions](#making-code-contributions)

Pay close attention to the section on making a pull request as this is how your contribution can be added to this repository.⬇️
* [**Making a Pull reuqest**](#making-a-pull-request)

There are two ways to contribute to this repository.

### Making non-code contributions
- Navigate into the contributions folder. You should see a file named 'Tips_and_tricks.md'.
You can add a random tip or trick that may be useful for the M25 community and commit it.
It will be reviewed and count towards your hacktoberfest challenge.
You need to make a total of four pull requests to complete this challenge.

- You can also contribute by adding more information to the readme.md or contributing.md file. This could be fixing a grammatical error or typo. (Note: It has to be a significant change though)

- In the contributions folder, we have a file named 'python_questions.md' and a folder called 'answers.

To participate, you can:
#### Put in a fun question in the python_questions.md file that you'll love other M25s to answer.
* It should be a question that can be solved by writing python code.
* It may be a question based on an HC from class or a random algorithm question.
* Your question should have a unique number so that it is easy to identify the corresponding solution.
For example: Your question can be called 'question 1' or even question 1043' (just make sure it's a reasonable number)

### Making code contributions
#### Answer a question in the python_questions.md file.
You can also contribute by providing a python solution to any question in the python_questions file.
* Your solution should be written in python.
* You should make it well-commented so others can benefit from your code.
* You can answer a question that has already been answered if you provide a diferent solution. In other words, there can be multiple answers to a question.
* **Write your code in a python_file and upload it to the answers folder above**
* Your file name should be prefixed with the question number you are answering.
**For example if your code is an answer to 'question 1', then you answer file should be named '1_name.py'.**
* Last but not least, make sure your code actually works to solve the problem!


## Making a pull request

So we have gone through why and how we can make contributions. Let's discuss how to contribute to this repository.
Contributing to an open source repository is done via pull requests.

A [pull request](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) is basically a way to let others know that you have made a change to this repository.

We can all make changes that we want to this repository. In order for it to be organized, there is a step-by-step process on how to make a change to the document.

* First, you **fork** this repository. (This allows you to make your own copy of this repository).
![no image](.img/fork.jpeg)
Click that button to fork the repository. You should have the repo on your profile as ```YourUsername/M25-Hacktoberfest``` now.

* If you have some experience working with git and github, you can follow [these](#making-changes-from-git-and-github) set of instructions. If otherwise, use [these](#making-changes-from-github).

### Making changes from Git and GitHub.
- After forking the repository, you can clone the repository to your computer.
- Navigate to your profile and click on code here, and copy the link.
![no image](.img/fork.jpeg)
- Open a folder on your computer, and type in terminal or git
```
git clone https://github.com/YourUsername/M25-Hacktoberfest.git
```
The link should be the one you copied from your profile.
- Next, set the main repository (this repository) as upstream.
```
git remote add upstream https://github.com/Ifeoluwakolopin/M25-Hacktoberfest.git
```
By adding upstream, you are basically pointing github to the main repository that you are connected to.
- Next, pull from the upstream repository
```
git pull upstream main
```
**NOTE: Since a lot of people are making changes to the repository, it is important to pull from the main repository before you start making any changes.**

By pulling, you are making sure that your repository is up-to-date with the main repository.

- Next, create a new branch where you will make your changes. For consistency, we will name our branch 'develop-yourUserName'

It is important to create a new branch so that your changes will not be conflicting with changes on the main branch. To create a new branch use
```
git checkout -b branchName
```
Like we said, our branch names should be your username joined with an hyphen to the word 'develop'. So:
```
git checkout -b develop-yourUserName
```

- Once you have done this, you should be on a new branch now.
- **You can now make any changes (additions/corrections) to the repository**

### After making changes:
Once you are done with your changes.
- Save all the changes you have made.
- Add your changes by running
```git add .```.
- Next commit your changes to Git.
You can add a message to identify your commit. For example
```git commit -m 'added question1'``` or ```git commit -m 'fixed typo in readme'```
- Once you have committed the changes to your repository. You should push your changes to GitHub.

Run:

```git push origin branchName```
'branchName' should be the name of the branch you just created.
Example: ```git push origin develop-yourUsername```

At this point, you have succesfully made your changes and pushed to GitHub!

One last stage remains! Go to the [main](https://github.com/Ifeoluwakolopin/M25-Hacktoberfest) repository on GitHub.
You should see a green button at the top that says, 'Compare and Pull Request'.

CLick that button to make a Pull Request (PR)!.

🎉🎉CONGRATULATIONS, YOU HAVE SUCCESFULLY MADE A PULL REQUEST🎉🎉

Follow these steps to make your pull request. remember, you need to make four PRs to complete the challenge.

Once your PR has been merged, Check your Hacktoberfest [dashboard](https://hacktoberfest.digitalocean.com/profile), you should see your PR in review.


#### Making Changes from GitHub

If you are not farmiliar with Git and GitHub, this is an helpful tutorial on how to make your PR directly from GitHub.