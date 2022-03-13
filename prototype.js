let tmp = document.createElement('body'); 
tmp.innerHTML = document.createNodeIterator(document.body, NodeFilter.SHOW_COMMENT, () => NodeFilter.FILTER_ACCEPT, false).nextNode().textContent;
let text = tmp.innerText.replace(' \n\t\n\t\t英语原文提示\n\t\tX\n\t\n\t\n\t\t    ', '');
document.getElementsByClassName('text_con')[0].textContent = text;