import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 5)
    dut.rst_n.value = 1

    # Caso 1: s_i = 0 → salida = lower nibble
    dut.ui_in.value = 0b10110011  # [7:4]=1011, [3:0]=0011
    dut.uio_in.value = 0b00000000 # s_i = 0

    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0b00000011

    # Caso 2: s_i = 1 → salida = upper nibble
    dut.uio_in.value = 0b00000001 # s_i = 1

    await ClockCycles(dut.clk, 1)
    assert dut.uo_out.value == 0b00001011