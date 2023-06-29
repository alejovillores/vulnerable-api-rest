import { Component } from '@angular/core';

@Component({
	selector: 'app-login-service',
	templateUrl: './login-service.component.html',
	styleUrls: ['./login-service.component.css']
})
export class LoginServiceComponent {

	private username: string = '';

	setUsername(username: string) {
		this.username = username;
	}

	getUsername() {
		return this.username;
	}
}