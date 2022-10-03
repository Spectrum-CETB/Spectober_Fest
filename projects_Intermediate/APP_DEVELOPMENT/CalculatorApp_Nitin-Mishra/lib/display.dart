import 'package:flutter/material.dart';

class Display extends StatelessWidget {
  const Display({Key? key, this.value = ''}) : super(key: key);

  final String value;

  @override
  Widget build(BuildContext context) {
    return Padding(
        padding: const EdgeInsets.all(20),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.end,
          children: <Widget>[
            Text(
              value,
              style: const TextStyle(
                  fontFamily: 'Avenir',
                  fontSize: 40,
                  fontWeight: FontWeight.bold),
            ),
          ],
        ));
  }
}
