.data
temp_measurement: .word 132
temp_upper: .word 150
temp_lower: .word  100

.text

error:
  /* Send a signal to a connected monitoring device. */
  /* Turn on a red LED. */
  bx lr

cool:
  /* Check if cool is already enabled. */
  and r3, r7, #2
  cmp r3, #2
  /* If yes, go to error. */
  beq error
  /* if no, enable. */
  and r7, r7, #2
  bx lr

heat:
  /* Check if heat is already enabled. */
  and r3, r7, #4
  cmp r3, #4
  /* If yes, go to error. */
  beq error
  /* if no, enable. */
  and r7, r7, #4
  bx lr
  bx lr

.global main
main:
  /* Check temperature reading. */
  ldr r1, =temp_measurement

  /* If equal or above temp_upper, call cool. */
  ldr r2, =temp_upper
  ldr r2, [r2]
  cmp r1, r2
  bge cool

  /* If equal or lower temp_lower, call heat. */
  ldr r2, =temp_lower
  ldr r2, [r2]
  cmp r1, r2
  ble heat

  /* If neither, continue. */
  bx lr
