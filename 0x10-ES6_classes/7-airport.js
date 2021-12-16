const util = require('util');

export default class Airport {
  constructor(name, code) {
    if (typeof name === 'string') this._name = name;
    if (typeof code === 'string') this._code = code;
  }

  // custom string representation of Airport
  [util.inspect.custom]() {
    return `${this.constructor.name} [${this._code}] { _name: '${this._name}', _code: '${this._code}' }`;
  }
}
