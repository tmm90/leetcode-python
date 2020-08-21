SCRIPT_DIR=$(realpath $(dirname ${BASH_SOURCE[0]}))
SRC_DIR=$(dirname $(realpath $SCRIPT_DIR))/src

# 创建并打开文件
function __lco(){
  output=`python3 $SCRIPT_DIR/leetcode_web_helper.py create_file $1`
  if [ $? == 0 ]; then
    src_file=`echo $output | grep -o -P "\d{4}_[-0-9a-z]*.py"`
    vim $SRC_DIR/$src_file
  else
    echo $output
  fi
}

alias lco="__lco" 
