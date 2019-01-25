
var widget = uploadcare.Widget('[role=uploadcare-uploader]');
var progressBar = document.getElementById('progress')
widget.onChange(function (fileInstance){
     fileInstance.progress(function (info){
        progressBar.innerText = Math.round(info.progress * 100) + '%';
  });
});