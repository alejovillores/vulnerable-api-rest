import { Component } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { MatDialog } from '@angular/material/dialog';
import { SuccessPopupComponent } from '../success-popup/success-popup.component';
import { GenericPopupComponent } from '../generic-popup/generic-popup.component';

@Component({
	selector: 'app-form',
	templateUrl: './form.component.html',
	styleUrls: ['./form.component.css']
})

export class FormComponent {

	app_name: string = '';
	username: string = '';
	password: string = '';
	showAppNameIsRequired: boolean = false;
	showUsernameIsRequired: boolean = false;
	showPasswordIsRequired: boolean = false;

	constructor(private http: HttpClient, private dialog: MatDialog) { }

	send() {

		if (this.app_name == '') { this.showAppNameIsRequired = true };
		if (this.username == '') { this.showUsernameIsRequired = true };
		if (this.password == '') { this.showPasswordIsRequired = true };

		if (this.app_name != '' && this.username != '' && this.password != '') {

			this.showAppNameIsRequired = false;
			this.showUsernameIsRequired = false;
			this.showPasswordIsRequired = false;

			let url = 'http://localhost:5000/password';

			const data = {
				app_name: this.app_name,
				app_username: this.username,
				password: this.password,
			};

			const headers = new HttpHeaders().set('Content-Type', 'application/json');
			const options = { headers, withCredentials: true };

			this.http.post(url, data, options).subscribe(
				response => {
					this.dialog.open(SuccessPopupComponent, {
						data: { appName: this.app_name, username: this.username, password: this.password },
						width: '400px'
					});
				},
				error => {
					this.dialog.open(GenericPopupComponent, {
						data: { title: 'Error', message: 'Error while adding the password' },
						width: '400px'
					});
				}
			);
		}
	}
}
