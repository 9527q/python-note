# GIT

## 常用命令

命令 | 示例 | 说明
-|:-:|-
clone | `git clone ssh或http链接` | 使用ssh无需用户名密码，本机需要有ssh服务并且将公钥添加到Git代码服务器，http无需事先设置什么，使用时需要填写用户名和密码，clone后本地只有一个master分支，本地分支和远程分支是互相独立的
branch | `git branch` | 查看本地分支，当前分支用‘*’+‘绿色’标出（-r查看远程分支，-a查看本地和远程所有分支）
 | `git branch -d <branch>` | 删除分支
 | `git branch --set-upstream-to=origin/<branch> <branch>` | 为分支创建跟踪信息，即令一个本地分支跟踪某个远程分支（pull和push的对象）（分支名可以不同）
checkout | `git checkout <branch>` | 切换本地分支
 | `git checkout -b <branch>` | 创建并切换到分支
 | `git checkout -b <branch> origin/<branch>` | 创建跟踪远程分支的本地分支且切换到此分支（最好同名，以后清晰且push不会乱）
diff | `git diff` | 对于本地仓库来说工作区的改动情况
 | `git diff branch1 branch2` | 对于分支1来说分支2的改动，本地分支或远程分支均可
 | `git diff path1 path2` | 比较多个路径或文件（不是他们之间）的改动情况
blame | `git blame path/file` | 查看代码编写者（具体文件）
add | `git add path/file` | 谨慎使用 `git add .` 有风险把不该提交的东西提交
commit | `git commit -m "some comment"` | 把暂存区的改动提交为一个版本
| `git commit --amend` | 修改上一次commit，内容是当前的暂存区，可以编辑提交内容比如刚刚commit的-m内容没写好想重新写比如有个小地方要改一下还不至于来一个新的commit
rebase | `git rebase -i adsf02d^` | 把这个版本之后的几个commit合并为一个，pick表示保留，f表示合并且不保留说明，然后末行模式执行x即可。

## 版本回退 git reset

- 回退版本：`git reset HEAD^`：一个 ^ 表示一个版本，可以多个
  - `git reset HEAD～n`：同上
  - `git reset commit-id`：回退到指定版本，版本号可以是全的也可以是7位的
  - 如果 HEAD 指针指向的是 master 分支，那么 HEAD 还可以换成 master
  - 如果不加参数，实际上使用的是默认的参数 mixed
  - 三个参数
    - soft 参数：`git reset --soft HEAD～1` 意为将版本库软回退1个版本
      > **软回退**表示将本地版本库的头指针全部重置到指定版本，且将这次提交之后的所有变更都移动到暂存区
    - 默认的mixed参数：`git reset HEAD～1` 意为将版本库回退1个版本，将本地版本库的头指针全部重置到指定版本，且会重置暂存区，即这次提交之后的所有变更都移动到未暂存阶段
    - hard参数：`git reset --hard HEAD～1` 意为将版本库回退1个版本，但是不仅仅是将本地版本库的头指针全部重置到指定版本，也会重置暂存区，并且会将工作区代码也回退到这个版本
    - **注意**soft参数与默认参数都不会修改工作区代码，只有hard参数才会修改工作区代码。
- 回退远程的个人分支版本：先把本地回退，再强制push到远程 `git push -f`
- 把**暂存区回退到工作区**（即保留改动）：`git reset HEAD filename`

## 查看版本

`git log -n`：查看最近的 n 次提交