import 'package:flutter/material.dart';
import 'calculator.dart';
import 'button.dart';
import 'rows.dart';

class CalculatorButtons extends StatelessWidget {
  CalculatorButtons({Key? key, required this.onTap}) : super(key: key);

  final CalculatorButtonTapCallback onTap;
  final calculatorButtonRows = [
    ['7', '8', '9', Calculations.DIVIDE],
    ['4', '5', '6', Calculations.MULTIPLY],
    ['1', '2', '3', Calculations.SUBTRACT],
    [Calculations.DECIMAL, '0', '00', Calculations.ADD],
    [Calculations.CLEAR, Calculations.EQUAL]
  ];

  @override
  Widget build(BuildContext context) {
    return Column(
        children: calculatorButtonRows.map((calculatorRowButtons) {
      return CalculatorRow(
        buttons: calculatorRowButtons,
        onTap: onTap,
      );
    }).toList());
  }
}
