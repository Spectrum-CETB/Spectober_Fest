import 'package:flutter/material.dart';
import 'calculator.dart';

class History extends StatelessWidget {
  const History({Key? key, required this.operations}) : super(key: key);

  final List<String> operations;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'History',
          style: TextStyle(fontFamily: 'Oswald'),
        ),
        backgroundColor: Colors.green,
        centerTitle: false,
      ),
      body: Center(
        child: _operationsList(operations),
      ),
    );
  }

  Widget _operationsList(List<String> operations) {
    return ListView.builder(
      itemCount: operations.length,
      itemBuilder: (BuildContext context, int i) {
        return ListTile(
          title: Text(operations[i]),
          onTap: () {
            Navigator.pop(context, operations[i]);
          },
          leading: Container(
            decoration: BoxDecoration(
              border: Border.all(color: Colors.red, width: 2.0),
            ),
            padding: const EdgeInsets.all(5),
            child: Text(
              Calculator.parseString(operations[i]),
              style: const TextStyle(
                  fontFamily: 'Nunito',
                  fontSize: 18,
                  fontWeight: FontWeight.bold),
            ),
          ),
        );
      },
    );
  }
}
