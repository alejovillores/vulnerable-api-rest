import { Component, Inject } from '@angular/core';
import { MAT_DIALOG_DATA } from '@angular/material/dialog';

@Component({
	selector: 'app-success-popup',
	templateUrl: './success-popup.component.html',
	styleUrls: ['./success-popup.component.css']
})
export class SuccessPopupComponent {
	appName: any;
	username: any;
	password: any;

	constructor(@Inject(MAT_DIALOG_DATA) public data: any) { }

	ngOnInit() {
		this.appName = this.data.appName;
		this.username =this.data.username;
		this.password = this.data.password;
	}
}