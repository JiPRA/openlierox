#ifndef OLX_IPRINTOUTFCT_H
#define OLX_IPRINTOUTFCT_H

#include <string>

struct PrintOutFct {
	virtual ~PrintOutFct() {}
	virtual void print(const std::string&) const = 0;
};

struct NullOut : PrintOutFct { void print(const std::string&) const {} };

#endif // OLX_IPRINTOUTFCT_H
