// A JavaScript script that adds, removes and clears LI elements
// from a list when the user clicks

const $ = window.$;
$('#add_item').click(function() {
  $('.my_list').append('<li>Item</li>');
});
$('#remove_item').click(function() {
  $('.my_list li:last-child').remove();
});
$('#clear_list').click(function() {
  $('.my_list').empty();
});
