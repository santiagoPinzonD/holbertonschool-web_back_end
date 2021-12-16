export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // Overriding default getter for [Symbol.species] with constructor (this)
  static get [Symbol.species]() {
    return this;
  }

  // Standard species pattern -> use this.constructor as the constructor for a new instance
  cloneCar() {
    const c = this.constructor;
    return new c[Symbol.species](this._brand, this._motor, this._color);
  }
}
