@echo off

D:
cd D:\workspace\python_workspace\01_cafeCrawler
python naverCafeWriteAll.py
python naverCafeReplyAll.py

cd D:\workspace\010_crawler_naverCafe2

Rscript src/03_preprocessing.R

git add data/naverCafeReply_A.xlsx
git add data/naverCafeWrite_A.xlsx
git commit -m "collected data"

git add out/all_frame.csv
git commit -m "publishing data"

git push

Rscript dash_executor.R

exit
