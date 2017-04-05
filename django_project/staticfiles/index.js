$('.wysiwyg-controls a').on('click', function(e) {

  e.preventDefault();
  document.execCommand($(this).data('role'), false);
});
