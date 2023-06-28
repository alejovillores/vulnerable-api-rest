import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GenericPopupComponent } from './generic-popup.component';

describe('GenericPopupComponent', () => {
  let component: GenericPopupComponent;
  let fixture: ComponentFixture<GenericPopupComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [GenericPopupComponent]
    });
    fixture = TestBed.createComponent(GenericPopupComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
