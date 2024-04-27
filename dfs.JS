var xpathResult = document.evaluate("/html/body/div[2]/div[2]/div[3]/div[5]/div/form/div/div[2]/table/tbody[1]/tr[1]/td/input", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
var inputElement = xpathResult.singleNodeValue;

// 선택한 input 요소가 있는지 확인
if (inputElement) {
    // input 요소의 값을 빈 문자열로 설정하여 내용 지우기
    inputElement.value = "";
} else {
    console.error("Input element not found!");
}


var iframe = document.getElementById('content_IFRAME');

console.log(iframe)

// iframe 내부 document 가져오기
var iframeDocument = iframe.contentDocument || iframe.contentWindow.document;

// iframe 내부 document에서 body 요소 선택
var xpathResult = iframeDocument.evaluate("/html/body", iframeDocument, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
var bodyElement = xpathResult.singleNodeValue;

// body 요소가 있는지 확인
if (bodyElement) {
    // body 요소의 내용을 지우기
    bodyElement.innerHTML = "";
} else {
    console.error("Body element inside iframe not found!");
}