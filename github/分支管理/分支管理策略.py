'''
通常，合并分支时，如果可能，Git会用Fast forward模式，但这种模式下，删除分支后，会丢掉分支信息。

如果要强制禁用Fast forward模式，Git就会在merge时生成一个新的commit，这样，从分支历史上就可以看出分支信息。

下面我们实战一下--no-ff方式的git merge：

首先，仍然创建并切换dev分支：

$ git checkout -b dev
Switched to a new branch 'dev'
修改readme.txt文件，并提交一个新的commit：

$ git add readme.txt
$ git commit -m "add merge"
[dev 6224937] add merge
 1 file changed, 1 insertion(+)
现在，我们切换回master：

$ git checkout master
Switched to branch 'master'
准备合并dev分支，请注意--no-ff参数，表示禁用Fast forward：

$ git merge --no-ff -m "merge with no-ff" dev
Merge made by the 'recursive' strategy.
 readme.txt |    1 +
 1 file changed, 1 insertion(+)
因为本次合并要创建一个新的commit，所以加上-m参数，把commit描述写进去。

合并后，我们用git log看看分支历史：

$ git log --graph --pretty=oneline --abbrev-commit
*   7825a50 merge with no-ff
|\
| * 6224937 add merge
|/
*   59bc1cb conflict fixed
...
可以看到，不使用Fast forward模式，merge后就像这样：

git-no-ff-mode


0:00
/ 0:57


分支策略

在实际开发中，我们应该按照几个基本原则进行分支管理：

首先，master分支应该是非常稳定的，也就是仅用来发布新版本，平时不能在上面干活；

那在哪干活呢？干活都在dev分支上，也就是说，dev分支是不稳定的，到某个时候，比如1.0版本发布时，再把dev分支合并到master上，在master分支发布1.0版本；

你和你的小伙伴们每个人都在dev分支上干活，每个人都有自己的分支，时不时地往dev分支上合并就可以了。

所以，团队合作的分支看起来就像这样：

git-br-policy

小结

Git分支十分强大，在团队开发中应该充分应用。

合并分支时，加上--no-ff参数就可以用普通模式合并，合并后的历史有分支，能看出来曾经做过合并，而fast forward合并就看不出来曾经做过合并。
'''



'''
在视频中，我们可以看到commit6224937(分支dev)和commit596c1cb(分支master)合并成了commit7825a50.这是由于合并的时候采用了--no-ff选项。
但是，commit6224937(分支dev)是commit596clcb（分支master)的下一次提交，是对master内容的一次更改，两次提交合并后的内容应该和commit6224937一模一样，
既然内容一模一样，为什么使用--no-ff选项后连commit id号都变了（变成了7825a50）？
希望能得到解答'''
'''

哥们，如果才用 ff 模式的，则直接把 master 的指针直接指向了 dev 分支的最新提交，这样两个分支的最新提交的 commit id 就是一样的。

如果采用 --no-ff 模式合并分支，由于不能直接把 master 指针直接指向 dev 分支的最新提交， master 分支只能进行一次提交操作，所以就会有内容一模一样，commit id 不同的问题。

简单地说就是 -no-ff 模式进行了一次新的 git commit 操作。

这也是为什么采用 -no-ff 模式要加入参数 -m 的原因。'''

'''
我看到廖老师在讲分支策略的时候，是说所有人的开发都在dev分支上进行，到了一定程度的时候，再往主线上面合并，所以主线分支的代码是比较稳定的。
但是我想问一下，这样的话，dev分支应该是大家共有的一个分支吧，但是如果通过：
git checkout -b branch_name or 
git branch branch_name
这两种方式建立的分支应该都是属于自己的本地分支。
那么，问题来了，怎么建立像dev这样的远程分支呢？这样大家才能在上面干活啊。。。'''

'''
在实际开发中，每个开发在公司远程仓库，都有一个对应每个人自己的远程分支，每次提交时教程里面讲git push 中master参数换成对应开发人员的分支就好了，
比如devloper1，控制版本上线的人比如运维人员，在远程仓库的服务器上，
再选择性地把某个开发人员的分支合并进真正的master实现上线
'''




