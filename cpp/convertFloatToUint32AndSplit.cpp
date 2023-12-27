// Example program
#include <iostream>
#include <string>

#include <cstdint>

void splitUInt32ToInt16(uint32_t phys_value, uint16_t& steering, uint16_t& turn) {
    // Extract steering and turn values from the uint32_t value
    turn = static_cast<uint16_t>((phys_value >> 16) & 0xFFFF);
    steering = static_cast<uint16_t>(phys_value & 0xFFFF);
    if (turn != 0) // 0: right 1: left
    {
        
        float st = -steering;
        std::cout << "st : " << st  << std::endl;
        printf("------------ left\n");
    }
    else
    {
        printf("------------ right\n");
    }
}

int main() {
	std::string phys_value_str = "4294966864";
	uint32_t  phys_value = std::stof(phys_value_str.c_str());
	//uint32_t  phys_value = 0x123;
	std::cout << "phys_value : " << phys_value  << std::endl;
	uint16_t steering = 0.0;
	uint16_t turn = 0.0;

	turn = static_cast<uint16_t>((phys_value >> 16) & 0xFFFF);
	steering = static_cast<uint16_t>(phys_value & 0xFFFF);
	std::cout << "turn  "<< turn<<std::endl;
	std::cout << "steering  "<< steering<<std::endl;
	if (turn != 0) // 0: right 1: left
	{
		int16_t decimal_value = static_cast<int16_t>(steering);

		// Set the sign bit
		decimal_value |= 0x8000;
		printf("------------ left\n");
		std::cout << "-- left .steering---#  " << decimal_value << std::endl;
	}
	else {
		
		printf("------------ right\n");
		std::cout << "-- right .steering---#  " <<steering << std::endl;
	}
            
    return 0;
}