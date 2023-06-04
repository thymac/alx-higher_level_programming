// A JavaScript script that fetches from https://fourtonfish.com/hellosalut/?lang=fr
// and displays the value of hello from that fetch in the HTML tag DIV#hello.

const $ = window.$;
$.get('https://fourtonfish.com/hellosalut/?lang=fr', function(data) {
  $('#hello').text(data.hello);
});
