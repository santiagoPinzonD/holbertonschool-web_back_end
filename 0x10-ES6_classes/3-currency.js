export default class Currency {
  constructor(code, name) {
    if (typeof (code) === 'string') this._code = code;
    else throw new Error(TypeError('code must be a String'));
    if (typeof (name) === 'string') this._name = name;
    else throw new Error(TypeError('name must be a String'));
  }

  set code(value) {
    if (typeof (value) === 'string') this._code = value;
    else throw new Error(TypeError('code must be a String'));
  }

  get code() {
    return this._code;
  }

  set name(value) {
    if (typeof (value) === 'string') this._name = value;
    else throw new Error(TypeError('name must be a String'));
  }

  get name() {
    return this._name;
  }

  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }
}
