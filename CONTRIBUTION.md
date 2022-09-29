## Contribution Guide

- Create a fork of the main repo [Offical Repo](https://github.com/Spectrum-CETB/Spectober_Fest).

- Then go to the repository in your own profile and click on **Code** as highlighted below and copy the _URL_ which is highlighted.

- Then on your system go the desired directory and create a duplicate by using the command

```bash
git clone https://github.com/Spectrum-CETB/Spectober_Fest
```

- Then the next step is to open your desired Code Editor and open up the terminal and switch to your branch

```bash
git checkout -b <new-branch name>
```

- To switch back to the original **main** branch type on the following code

```bash
git checkout main
```

- Go back to your branch and then make the changes and then stage up the changes and commit the changes and then push the changes to your own branch

```bash
# Stage up the Changes
git add .

# Commit the changes
git commit -m "Commit message as your choice"

# Push to your own branch
git push origin <Own branch>
```
