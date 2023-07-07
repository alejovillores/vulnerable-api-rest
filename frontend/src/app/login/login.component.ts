import { Component } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Router } from '@angular/router';
import { MatDialog } from '@angular/material/dialog';
import { GenericPopupComponent } from '../generic-popup/generic-popup.component';
import { LoginServiceComponent } from '../login-service/login-service.component';

@Component({
	selector: 'app-login',
	templateUrl: './login.component.html',
	styleUrls: ['./login.component.css']
})

export class LoginComponent {
	username: string = "";
	password: string = "";
	showUsernameIsRequired: boolean = false;
	showPasswordIsRequired: boolean = false;
	currentPassword: string = "";
	newPassword: string = "";
	showCurrentPasswordIsRequired: boolean = false;
	showNewPasswordIsRequired: boolean = false;

	constructor(private http: HttpClient, private router: Router, private dialog: MatDialog, private loginService: LoginServiceComponent) { }

	changePassword() {
		if (this.username == '') { this.showUsernameIsRequired = true };
		if (this.currentPassword == '') { this.showCurrentPasswordIsRequired = true };
		if (this.newPassword == '') { this.showNewPasswordIsRequired = true };

		if (this.username != '' && this.currentPassword != '' && this.newPassword != '') {

			this.showUsernameIsRequired = false;
			this.showCurrentPasswordIsRequired = false;
			this.showNewPasswordIsRequired = false;

			const data = {
				username: this.username,
				password: this.currentPassword
			};

			const headers = new HttpHeaders().set('Content-Type', 'application/json');
			const options = { headers, withCredentials: true };

			this.http.post('http://localhost:5000/login', data, options).subscribe(
				response => {
					this.http.post(`http://localhost:5000/password/reset`, {new_password: this.newPassword}, options).subscribe(
						response => {
							this.dialog.open(GenericPopupComponent, {
								data: { title: 'Success', message: 'Password successfully changed' },
								width: '400px'
							});
						});

				},
				error => {
					this.dialog.open(GenericPopupComponent, {
						data: { title: 'Error', message: 'Error in username or current password' },
						width: '400px'
					});
				}
			);
		}
	}

	login() {
		this.send('http://localhost:5000/login', false);
	}

	register() {
		this.send('http://localhost:5000/register', true)
	}

	send(url: string, isRegister: boolean) {

		if (this.username == '') { this.showUsernameIsRequired = true };
		if (this.password == '') { this.showPasswordIsRequired = true };

		if (this.username != '' && this.password != '') {

			this.showUsernameIsRequired = false;
			this.showPasswordIsRequired = false;

			const data = {
				username: this.username,
				password: this.password
			};

			const headers = new HttpHeaders().set('Content-Type', 'application/json');
			const options = { headers, withCredentials: true };

			this.http.post(url, data, options).subscribe(
				response => {
					if (isRegister) {
						this.dialog.open(GenericPopupComponent, {
							data: { title: 'Success', message: 'New user successfully created' },
							width: '400px'
						});
					} else {
						this.router.navigate(['/table']);
						this.loginService.setUsername(this.username);
					}
				},
				error => {
					let message;
					if (isRegister) { message = 'Error while registering new user' }
					else { message = 'Error while loging in' };

					this.dialog.open(GenericPopupComponent, {
						data: { title: 'Error', message: message },
						width: '400px'
					});
				}
			);
		}
	}

}