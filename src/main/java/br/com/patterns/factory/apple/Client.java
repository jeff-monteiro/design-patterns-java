package br.com.patterns.factory.apple;

import br.com.patterns.factory.apple.factory.IPhoneFactory;
import br.com.patterns.factory.apple.factory.IPhoneXFactory;

public class Client {
	
	public static void main(String[] args) {
		
		IPhoneFactory iphoneX = new IPhoneXFactory();
		iphoneX.orderIPhone();
		System.out.println("### Ordering an iPhone X");
		
		System.out.println("\n\n### Ordering an iPhone 11 HighEnd");
	}
}
