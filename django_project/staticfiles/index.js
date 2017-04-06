var text = document.forms[0].comment.value;
var text = document.getElementById("id_comment");
text = text.value;
text = text.replace(/\r?\n/g, '</p><p>');