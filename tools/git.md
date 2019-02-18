# GIT

## 常用命令

命令 | 示例 | 说明
-|-|-
clone | `git clone ssh或http链接` | 使用ssh无需用户名密码，本机需要有ssh服务并且将公钥添加到Git代码服务器，http无需事先设置什么，使用时需要填写用户名和密码，clone后本地只有一个master分支，本地分支和远程分支是互相独立的
branch | `git branch` | 查看本地分支，当前分支用‘*’+‘绿色’标出（-r查看远程分支，-a查看本地和远程所有分支）
 | `git branch -d <branch>` | 删除分支
 | `git branch --set-upstream-to=origin/<branch> <branch>` | 为分支创建跟踪信息，即令一个本地分支跟踪某个远程分支（pull和push的对象）（分支名可以不同）
checkout | `git checkout <branch>` | 切换本地分支
 | `git checkout -b <branch>` | 创建并切换到分支
 | `git checkout -b <branch> origin/<branch>` | 创建跟踪远程分支的本地分支且切换到此分支（最好同名，以后清晰且push不会乱）
diff | `git diff` | 对于本地仓库来说工作区的改动情况
 | `git diff branch1 branch2` | 对于分支1来说分支2的改动，本地分支或远程分支均可
blame | `git blame path/file` | 查看代码编写者（具体文件）
add | `git add path` | 谨慎谨慎谨慎使用`git add .`不然会把本地的不该提交的东西提交的
 | `git add path/file` | 
commit | `git commit --amend` | 修改上一次commit，内容是当前的暂存区，可以编辑提交内容比如刚刚commit的-m内容没写好想重新写比如有个小地方要改一下还不至于来一个新的commit（有可能是小失误没考虑周全）
rebase | `git rebase -i adsf02d^` | 把这个版本之后的几个commit合并为一个，pick表示保留，f表示合并且不保留说明，然后末行模式执行x即可。

## 常见问题

1. 版本回退
   1. 回退本地的版本：
        ```sh
        git reflog
        git reset --hard Obfafd
        ```
   2. 回退远程的个人分支版本
      1. 先把本地回退，再强制push到远程
            ```sh
            git push -f
            ```