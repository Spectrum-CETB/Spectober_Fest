import 'package:flutter/material.dart';
import 'button.dart';

class CalculatorRow extends StatelessWidget {
  const CalculatorRow({Key? key, required this.buttons, required this.onTap})
      : super(key: key);

  final List<String> buttons;
  final CalculatorButtonTapCallback onTap;

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceAround,
      children: rowButtons(),
    );
  }

  List<Widget> rowButtons() {
    List<Widget> rowButtons = [];

    for (var buttonText in buttons) {
      rowButtons.add(
        CalculatorButton(
          text: buttonText,
          onTap: onTap,
        ),
      );
    }

    return rowButtons;
  }
}
