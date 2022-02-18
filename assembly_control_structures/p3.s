.data
temp_measurement: .word 130
temp_upper: .word 150
temp_lower: .word  100

.text

error:
  /* Send a signal to a connected monitoring device. */
  /* Turn on a red LED. */
  mov r0, #0
  b end

all_off:
  and r3, r7, #6
  eor r7, r7, r7
  mov r0, #1
  b end

cool_on:
  /* Check if cool is already enabled. */
  and r3, r7, #2
  cmp r3, #2
  /* If yes, go to error. */
  beq error
  /* if no, enable. */
  and r7, r7, #2
  mov r0, #2
  b end

heat_on:
  /* Check if heat is already enabled. */
  and r3, r7, #4
  cmp r3, #4
  /* If yes, go to error. */
  beq error
  /* if no, enable. */
  and r7, r7, #4
  mov r0, #3
  b end

.global main
main:
  /* Check temperature reading. */
  ldr r1, =temp_measurement
  ldr r1, [r1]

  /* If equal or above temp_upper, call cool. */
  ldr r2, =temp_upper
  ldr r2, [r2]
  /* cmp subtracts r1 from r2 */
  cmp r1, r2
  bhs cool_on

  /* If equal or lower temp_lower, call heat. */
  ldr r2, =temp_lower
  ldr r2, [r2]
  cmp r1, r2
  bls heat_on

  /* If neither, continue. */
  b all_off
end:
  bx lr
