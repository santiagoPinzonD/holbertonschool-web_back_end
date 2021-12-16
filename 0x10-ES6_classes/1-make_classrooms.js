import ClassRoom from './0-classroom';

/**
 * Creates an array of three ClassRoom objects
 */
export default function initializeRooms() {
  return [
    new ClassRoom(19),
    new ClassRoom(20),
    new ClassRoom(34),
  ];
}
