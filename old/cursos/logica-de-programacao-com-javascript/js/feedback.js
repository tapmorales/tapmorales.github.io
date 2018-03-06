var feedback = {
	fechaFeedback: null,
	delay: 3000,
	init: function(msgOk, msgErr){
		msgOk = msgOk || 'Cadastro efetuado com sucesso';
		msgErr = msgErr || 'Desculpe, houve um erro no seu cadastro';
		if(this.getStatusFromUrl() === 'ok'){		
			this.show({'success': true, 'msg': msgOk});
		} else if(this.getStatusFromUrl() === 'err'){
			this.show({'success': false, 'msg': msgErr});
		}
	},
	close: function(){
		var feedbackContainer = document.querySelector('.feedback');
		feedbackContainer.classList.add('feedback--hide');
		feedbackContainer.classList.remove('feedback--show');

		if(feedback.fechaFeedback) clearTimeout(feedback.fechaFeedback);

		setTimeout(function(){
			feedbackContainer.remove();
			feedbackContainer = null;
		}, 500);

		window.location.href = window.location.origin + window.location.pathname;
	},
	getStatusFromUrl: function(){
		if(window.location.search.indexOf('status=ok') > 0){
			return 'ok';
		}
		if(window.location.search.indexOf('status=err') > 0){
			return 'err';
		}

		return false;
	},
	show: function(data){
		var teste = (data.success) ? 'feedback--success' : 'feedback--error';

		var bodyContainer = document.body;

		var divFeedback = document.createElement('div');
		divFeedback.setAttribute('class', 'feedback feedback--hide ' + teste);


		var str = '<p> '+ data.msg + '  </p>'+
					'<button class="close" onclick="feedback.close()">X</button>';

		bodyContainer.appendChild(divFeedback);
		divFeedback.innerHTML += str;

		

		setTimeout(function(){
			var feedbackContainer = document.querySelector('.feedback');
			feedbackContainer.classList.remove('feedback--hide');
			feedbackContainer.classList.add('feedback--show');
		}, 100);

		this.fechaFeedback = setTimeout(function(){
			feedback.close();
		}, feedback.delay);
	}
}