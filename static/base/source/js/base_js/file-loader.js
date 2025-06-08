document.getElementById('file-upload').onchange = function(e) {
  document.querySelector('.custom-file-upload').innerText = e.target.files[0].name || 'Нажмите сюда!';
};