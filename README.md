# Remove-pdf-breaks
As a novice, when reading pdfs of a new domain, we often copy some sentences to the translation site. However, the site will not automatically remove PDF line breaks, which makes each sentence incomplete and the translation inaccurate. And this small program solves this problem. 

## Requirement: 
On Linux, install xsel via package manager. For example, in Ubuntu:

    sudo apt-get install xsel
	
	
On Windows, win32clipboard and win32con are required, and there are all included in pywin32:

	pip install pywin32
	

## Usage:
  1) Copy some paragraphies from PDF;
  2) Run this py script in the terminal, then it will be run continously and remove the breaklines automatically until you stop it.
  3) OK, go to paste where you want. 
  

作为新手，看新领域文献时常常要复制内容到翻译网站，网站不会自动把pdf内换行符去掉，导致每句话不完整，翻译不准确。而这个小程序解决了这个问题。
## 使用方法：
  1) 从PDF复制所需要的段落；
  2) 在命令行中运行此脚本，之后该脚本会一直运行并且自动去除换行，直到手动停止。
  3) OK，去粘贴吧。 
