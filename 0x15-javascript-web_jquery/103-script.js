// A JavaScript script that fetches and prints how to say
// "Hello" depending on the language

const $ = window.$;
$('#btn_translate, #language_code').keypress(function(event) {
  if (event.keyCode === 13 || event.which === 13) {
    const langCode = $('#language_code').val();
    $.get('https://www.fourtonfish.com/hellosalut/hello/${langCode}', function(data) {
      $('#hello').text(data.hello);
    });
  }
});
