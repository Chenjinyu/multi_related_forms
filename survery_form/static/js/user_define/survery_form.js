/*
 author: Chen Jinyu
 email: jinyuc@fireracker.com
 date: 06/30/2016
 */
var weburl = this.location.href.match(/http:\/\/([a-zA-Z0-9-_\.]+\/)+/gi);
var webpath = this.location.href.match(/http:\/\/([a-zA-Z0-9-_\.]+\/)/gi);
if (weburl == null) {
    weburl = 'http://127.0.0.1:8080/onlineform/';
}


$(document).ready(function() {
			
	function csrfSafeMethod(method) {
		// these HTTP methods do not require CSRF protection
		return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}

	function cancel_del()
	{
		bootbox.confirm("Do you want to cancel this form? If yes, all of information would be lost.", function(result) {
		  if(result){
			$.ajax({
				type: 'POST',
				url: '/onlineform/cancel_del/',
				error: function(data){},
				success: function(data){
					$(location).attr('href','/onlineform/');
				}
			});
	       }
    	});
  
	}

	$.ajaxSetup({
		beforeSend: function(xhr, settings) {
		var csrftoken = Cookies.get('csrftoken');
			if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		}
	});

	$('#store_cnl_btn').click(function() {
		cancel_del()
	});
	
	$('#br_cnl_btn').click(function() {
		cancel_del()
	});
	
	$('#mc_cnl_btn').click(function() {
		cancel_del()
	});
	
	$('#ml_cnl_btn').click(function() {
		cancel_del()
	});
	
	$('#nm_cnl_btn').click(function() {
		cancel_del()
	});
	
	$('#sc_cnl_btn').click(function() {
		cancel_del()
	});
	
	$('#wf_np_cnl_btn').click(function() {
		cancel_del()
	});
	
	$('#addi_cnl_btn').click(function() {
		cancel_del()
	});
	
});



