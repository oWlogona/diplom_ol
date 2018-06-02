$(document).ready(function(){
	var form = $('#form_buying_product');

	function basket_updating(product_id, amount, is_delete){
		var data = {};
		data.product_id = product_id;
		data.amount = amount;
		var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
		data['csrfmiddlewaretoken'] = csrf_token;

		if(is_delete){
			data["is_delete"] = true;
		}

		var url = form.attr("action");

		console.log(data)
		$.ajax({
			url: url,
			type: 'POST',
			data: data,
			cache: true,
			success: function(data){
				console.log('OK');
				if(data.products_total_number || data.products_total_number == 0){
					$('#products_total_number').text("(" + data.products_total_number + ")");
					$('.basket_items ul').html("");
					$.each(data.products, function(k, v){
						$('.basket_items ul').append('<li>'+ v.name + ', ' + v.number + 'шт. ' + 'price: ' 
							+ v.price_per_item + 'грн. '  + '<a class="delete_item" data-product_id="'+v.id+'">x</a>' + '</li>')
					})
				}
			},
			error: function(){
				console.log('error');
			}
		})
	}

	form.on('submit', function(e){
		e.preventDefault();
		var amount = $('#amount').val();
		var submit_btn = $('#submit_btn');
		var product_id = submit_btn.data("product_id");
		var product_name = submit_btn.data("name");
		var product_price = submit_btn.data("price");

		basket_updating(product_id, amount, is_delete=false);
	})


	function showingBasket(){
		$('.basket_items').removeClass('hidden');
	}

	$('.basket_container').mouseover(function(){
		showingBasket();
	})

	$('.basket_container').mouseout(function(){
		showingBasket();
	})

	$(document).on('click', '.delete_item', function(e){
		e.preventDefault();
		product_id = $(this).data('product_id');
		amount = 0;
		basket_updating(product_id, amount, is_delete=true);
	});

	function calculate_basket_amount(){
		var total_order = 0;
		$('.total_product_in_amount').each(function(){
			total_order += parseFloat($(this).text());
		});
		$('.total_order').text(total_order.toFixed(1))
	};

	$(document).on('change', '.product_in_basket_number', function(){
		console.log('test')
		var current_amount = $(this).val();
		var current_tr = $(this).closest('tr');
		var current_price = parseFloat(current_tr.find('.product_price').text());
		var total_amount = current_amount * current_price;
		current_tr.find('.total_product_in_amount').text(total_amount.toFixed(1));
		calculate_basket_amount();
	})
	
	calculate_basket_amount();
});