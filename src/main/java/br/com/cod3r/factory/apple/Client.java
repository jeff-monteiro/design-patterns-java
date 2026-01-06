package br.com.cod3r.factory.apple;

import br.com.cod3r.factory.apple.factory.IPhoneFactory;
import br.com.cod3r.factory.apple.factory.IPhoneXFactory;

public class Client {
	
	public static void main(String[] args) {
		
		IPhoneFactory iphoneX = new IPhoneXFactory();
		System.out.println("### Ordering an iPhone X");
		
		System.out.println("\n\n### Ordering an iPhone 11 HighEnd");
	}
}
