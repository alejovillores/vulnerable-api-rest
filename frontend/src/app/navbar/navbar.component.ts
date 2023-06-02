import { Component } from '@angular/core';
import { LoginServiceComponent } from '../login-service/login-service.component';

@Component({
	selector: 'app-navbar',
	templateUrl: './navbar.component.html',
	styleUrls: ['./navbar.component.css']
})
export class NavbarComponent {

	username: string = '';

	constructor(private loginService: LoginServiceComponent) {}

	ngOnInit() {
		this.username = this.loginService.getUsername();
	}

}