import { Component, Inject } from '@angular/core';
import { MAT_DIALOG_DATA } from '@angular/material/dialog';
import { DomSanitizer } from '@angular/platform-browser';

@Component({
	selector: 'app-success-popup',
	templateUrl: './success-popup.component.html',
	styleUrls: ['./success-popup.component.css']
})
export class SuccessPopupComponent {
	appName: any;
	username: any;
	password: any;

	constructor(@Inject(MAT_DIALOG_DATA) public data: any, private sanitizer: DomSanitizer) { }

	ngOnInit() {
		this.appName = this.sanitizer.bypassSecurityTrustHtml(this.data.appName);
		this.username = this.sanitizer.bypassSecurityTrustHtml(this.data.username);
		this.password = this.sanitizer.bypassSecurityTrustHtml(this.data.password);
	}
}
