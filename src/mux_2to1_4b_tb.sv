/*
* Instituto Tecnológico de Costa Rica
* Prof. Dr.-ing. Pablo Mendoza Ponce
* Rev. 1 28 July 2024
*/
module mux_2to1_4b_tb;
  timeunit 1ns;
  timeprecision 1ps;  

  logic [3:0] a_i;
  logic [3:0] b_i;
  logic       s_i;
  logic [3:0] q_o;


  mux_2to1_4b dut (.*);

  initial begin
    {s_i,a_i,b_i} = '0;
    repeat(2**9) begin
      #1;
      {s_i, a_i, b_i} = {s_i, a_i, b_i} + 1'b1;
    end
    #2 $stop;
  end
  
endmodule