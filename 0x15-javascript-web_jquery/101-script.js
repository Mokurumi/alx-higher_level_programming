$('#add_item').click(function () {
  const newItem = $('<li>Item</li>');
  $('UL.my_list').append(newItem);
});

$('#remove_item').click(function () {
  $('UL.my_list LI:last-child').remove();
});

$('#clear_list').click(function () {
  $('UL.my_list').empty();
});