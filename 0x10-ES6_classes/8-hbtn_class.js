export default class HolbertonClass {
  // returns this._size if class is casted into a number
  // returns this._location if class is casted into a string
  constructor(size, location) {
    if (typeof (size) === 'number') this._size = size;
    if (typeof (location) === 'string') this._location = location;
  }

  // to convert obj to a primitive value
  [Symbol.toPrimitive](hint) {
    if (hint === 'string') return this._location;
    if (hint === 'number') return this._size;
    return this;
  }
}
